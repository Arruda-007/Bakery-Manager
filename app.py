from flask import Flask, render_template, jsonify, send_file
import pandas as pd
import os
from dotenv import load_dotenv
from openai import OpenAI

# ======== CONFIGURAÇÕES INICIAIS ========
app = Flask(__name__)

# ✅ Carrega variáveis de ambiente (.env)
load_dotenv()

# ✅ Configura o cliente da OpenAI (caso exista chave)
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) if api_key else None


# ======== ROTAS PRINCIPAIS ========

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/iot')
def iot():
    return render_template('iot.html')


@app.route('/insights')
def insights():
    df = pd.read_csv('data/iot_data.csv')
    medias = {
        "temperatura": round(df["temperatura"].mean(), 1),
        "energia": round(df["energia"].mean(), 1),
        "umidade": round(df["umidade"].mean(), 1),
        "ocupacao": round(df["ocupacao"].mean(), 1),
        "gas": round(df["gas"].mean(), 1),
        "fumaca": round(df["fumaca"].mean(), 1),
        "luminosidade": round(df["luminosidade"].mean(), 1),
        "agua": round(df["agua"].mean(), 1),
        "nivel": round(df["nivel"].mean(), 1),
        "movimento": round(df["movimento"].mean() * 100, 1)  # movimento em %
    }
    return render_template('insights.html', medias=medias)



@app.route('/relatorios')
def relatorios():
    """
    Exibe a página de relatórios (contém botão de gerar e área de resultado).
    """
    return render_template('relatorios.html')


@app.route('/api/gerar_relatorio')
def api_gerar_relatorio():
    """
    Gera relatório técnico com base nos dados do CSV.
    Se houver chave da OpenAI, usa GPT; senão, gera localmente.
    """
    df = pd.read_csv('data/iot_data.csv')

    resumo = {
        "temperatura_media": round(df["temperatura"].mean(), 1),
        "temperatura_max": round(df["temperatura"].max(), 1),
        "energia_total": round(df["energia"].sum(), 1),
        "ocupacao_media": round(df["ocupacao"].mean(), 1),
        "gases_detectados": int((df["gas"] > 250).sum()),
        "fumaca_detectada": int((df["fumaca"] > 180).sum())
    }

    # ===== Geração local de relatório (fallback) =====
    def gerar_relatorio_local(resumo):
        partes = []
        tmed, tmax = resumo["temperatura_media"], resumo["temperatura_max"]

        if tmed > 210:
            partes.append(f"A temperatura média de {tmed}°C está acima do ideal. Verifique ajustes nos fornos.")
        elif tmed < 180:
            partes.append(f"A temperatura média de {tmed}°C está abaixo do esperado — possível falha nos queimadores.")
        else:
            partes.append(f"A temperatura média de {tmed}°C está dentro da faixa esperada de operação.")
        partes.append(f"A maior temperatura registrada foi {tmax}°C.")

        energia = resumo["energia_total"]
        partes.append(f"O consumo total de energia foi de {energia} kWh. Avalie horários de pico.")

        ocup = resumo["ocupacao_media"]
        if ocup > 90:
            partes.append(f"A ocupação média de {ocup}% sugere alta demanda — considere reforçar a equipe.")
        elif ocup < 40:
            partes.append(f"A ocupação média de {ocup}% indica baixa movimentação — avalie promoções.")
        else:
            partes.append(f"A ocupação média de {ocup}% está dentro do esperado.")

        gases, fuma = resumo["gases_detectados"], resumo["fumaca_detectada"]
        if gases > 0 or fuma > 0:
            partes.append(f"Foram detectados {gases} casos de gás e {fuma} de fumaça — realizar inspeção imediata.")
        else:
            partes.append("Nenhum vazamento de gás ou fumaça registrado.")

        partes.append("Recomenda-se revisar manutenção dos fornos e calibrar sensores periodicamente.")
        return " ".join(partes)

    # ===== Tenta gerar com GPT (se houver chave) =====
    try:
        if client:
            prompt = f"""
            Você é um analista técnico da Smart Bakery 4.0.
            Gere um relatório técnico sobre os seguintes dados:
            {resumo}
            Use linguagem profissional e inclua recomendações.
            """

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é um especialista em análise de dados IoT."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=400,
                temperature=0.7
            )
            texto_relatorio = response.choices[0].message.content.strip()
        else:
            texto_relatorio = gerar_relatorio_local(resumo)

    except Exception as e:
        print("⚠️ Erro com OpenAI, usando relatório local:", e)
        texto_relatorio = gerar_relatorio_local(resumo)

    return jsonify({"relatorio": texto_relatorio})


@app.route('/download_csv')
def download_csv():
    return send_file('data/iot_data.csv', as_attachment=True)


@app.route('/historico')
def historico():
    return render_template('historico.html')


@app.route('/api/historico')
def api_historico():
    df = pd.read_csv('data/iot_data.csv')
    df = df.tail(100)  # Mostra apenas as últimas 100 linhas
    return df.to_json(orient='records')


@app.route('/sprints')
def sprints():
    return render_template('sprints.html')


# ======== EXECUÇÃO ========
if __name__ == '__main__':
    app.run(debug=True)
