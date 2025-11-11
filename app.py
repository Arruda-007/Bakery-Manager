from flask import Flask, render_template, jsonify, send_file
import pandas as pd
import os
from dotenv import load_dotenv
import google.generativeai as genai

# ======== CONFIGURAÇÕES INICIAIS ========
app = Flask(__name__)

# Carrega variáveis de ambiente (.env)
load_dotenv()

# Configura Gemini com a chave do .env
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ======== FUNÇÕES AUXILIARES ========
def gerar_resumo_iot():
    """Lê o CSV e retorna um resumo dos dados principais"""
    df = pd.read_csv("data/iot_data.csv")
    resumo = {
        "temperatura_media": round(df["temperatura"].mean(), 1),
        "temperatura_max": round(df["temperatura"].max(), 1),
        "energia_total": round(df["energia"].sum(), 1),
        "ocupacao_media": round(df["ocupacao"].mean(), 1),
        "gases_detectados": int((df["gas"] > 250).sum()),
        "fumaca_detectada": int((df["fumaca"] > 180).sum())
    }
    return resumo


# ======== ROTA: GERAR RELATÓRIO ========
@app.route("/api/gerar_relatorio")
def api_gerar_relatorio():
    resumo = gerar_resumo_iot()
    prompt = f"""
    Gere um **relatório técnico detalhado** da Smart Bakery 4.0.
    Use títulos, seções e marcadores em Markdown.
    Analise os seguintes dados: {resumo}

    Estruture assim:
    ## Relatório Técnico — Smart Bakery 4.0
    **Objetivo:** Explique brevemente a finalidade do relatório.
    **Análise dos Dados:** Interprete os valores e identifique possíveis problemas.
    **Conclusões e Recomendações:** Sugira melhorias ou ações futuras.

    Mantenha um tom profissional, técnico e organizado.
    """

    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)
        texto_relatorio = response.text
    except Exception as e:
        texto_relatorio = f"[ERRO Gemini] {e}"

    return jsonify({"relatorio": texto_relatorio})


# ======== ROTA: LIÇÕES APRENDIDAS ========
@app.route("/api/licoes_aprendidas")
def api_licoes_aprendidas():
    resumo = gerar_resumo_iot()
    prompt = f"""
    Gere um **relatório de Lições Aprendidas** para o projeto Smart Bakery 4.0.
    Formate em Markdown com subtítulos e tópicos.

    ## Lições Aprendidas — Smart Bakery 4.0
    **Resumo do Projeto:** Breve explicação sobre o objetivo do sistema.
    **Principais Desafios:** Dificuldades encontradas durante o desenvolvimento.
    **Soluções Implementadas:** Como os desafios foram superados.
    **Aprendizados Técnicos e de Equipe:** Principais aprendizados adquiridos.
    **Recomendações Futuras:** Sugestões de melhoria e próximos passos.

    Baseie-se nos seguintes dados: {resumo}
    """

    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)
        texto_licoes = response.text
    except Exception as e:
        texto_licoes = f"[ERRO Gemini] {e}"

    # 🔹 usa a mesma chave "relatorio" para compatibilidade com relatorios.js
    return jsonify({"relatorio": texto_licoes})


# ======== DEMAIS PÁGINAS ========
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/iot")
def iot():
    return render_template("iot.html")

@app.route("/insights")
def insights():
    df = pd.read_csv("data/iot_data.csv")
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
        "movimento": round(df["movimento"].mean() * 100, 1)
    }
    return render_template("insights.html", medias=medias)

@app.route("/relatorios")
def relatorios():
    return render_template("relatorios.html")

@app.route("/download_csv")
def download_csv():
    return send_file("data/iot_data.csv", as_attachment=True)

@app.route("/historico")
def historico():
    return render_template("historico.html")

@app.route("/api/historico")
def api_historico():
    df = pd.read_csv("data/iot_data.csv")
    df = df.tail(100)
    return df.to_json(orient="records")

@app.route("/sprints")
def sprints():
    return render_template("sprints.html")

@app.route("/avf4")
def avf4():
    return render_template("avf4.html")


# ======== EXECUÇÃO ========
if __name__ == "__main__":
    app.run(debug=True)
