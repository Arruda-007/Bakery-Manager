import csv
import random
from datetime import datetime, timedelta

# ===== CONFIGURAÇÕES =====

# Tempo total = 1h 20min de dados contínuos
output_file = "data/iot_data.csv"
num_registros = 500          # total de registros
intervalo_segundos = 10      # intervalo entre leituras (10s)

# Sensores da padaria inteligente
sensores = [
    "temperatura", "energia", "ocupacao", "umidade", "gas",
    "fumaca", "luminosidade", "agua", "nivel", "movimento", "peso"
]

# ===== GERAÇÃO DE VALORES =====
def gerar_valor(sensor):
    ranges = {
        "temperatura": (170, 220),     # °C
        "energia": (25, 40),           # kWh
        "ocupacao": (30, 95),          # %
        "umidade": (40, 85),           # %
        "gas": (0, 300),               # ppm
        "fumaca": (0, 200),            # ppm
        "luminosidade": (100, 800),    # lux
        "agua": (5, 25),               # L/min
        "nivel": (50, 100),            # %
        "movimento": (0, 1),           # 0 = sem movimento, 1 = detectado
        "peso": (200, 500)             # kg de massa
    }
    vmin, vmax = ranges[sensor]
    valor = round(random.uniform(vmin, vmax), 1)
    return int(valor) if sensor == "movimento" else valor

# ===== GERA OS DADOS =====
inicio = datetime.now()
dados = []

for i in range(num_registros):
    timestamp = inicio + timedelta(seconds=i * intervalo_segundos)
    linha = {"timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S")}
    for s in sensores:
        linha[s] = gerar_valor(s)
    dados.append(linha)

# ===== SALVA EM CSV =====
with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["timestamp"] + sensores)
    writer.writeheader()
    writer.writerows(dados)

print(f"✅ Arquivo gerado com sucesso!")
print(f"📊 Total de registros: {num_registros}")
print(f"💾 Arquivo salvo em: {output_file}")
