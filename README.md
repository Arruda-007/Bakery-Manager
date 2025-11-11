# 🍞 Bakery Manager 4.0 — Sistema IoT e Relatórios Inteligentes  

### 📚 Gestão de Projetos — Análise e Desenvolvimento de Sistemas  

O **Bakery Manager 4.0** é um sistema inteligente de monitoramento IoT e análise de dados voltado para padarias modernas.  
Ele permite acompanhar, em tempo real, o funcionamento dos fornos, sensores ambientais e consumo energético, além de gerar relatórios automáticos com o apoio de **IA (Gemini)**.

---

## 🚀 Funcionalidades Principais

### 🧩 Módulo 1 — Estrutura Base
- Interface desenvolvida em **Flask (Python)** e **HTML/CSS/JavaScript**.
- Sistema modular com páginas integradas (IoT, Insights, Relatórios, Histórico etc).

### 🌡️ Módulo 2 — Monitoramento IoT
- Simulação de sensores:
  - Temperatura  
  - Umidade  
  - Consumo de energia  
  - Ocupação da loja  
  - Luminosidade  
  - Fluxo de água  
  - Nível do reservatório  
  - Gás e fumaça  
  - Presença e movimento  
- Atualização dinâmica dos gráficos via **Chart.js**.
- Visualização de dados históricos com base em `iot_data.csv`.

### 🧠 Módulo 3 — Análises e Insights
- Geração automática de **KPIs** médias dos sensores.
- Gráficos comparativos (ex.: energia antes e depois da automação).
- Textos narrativos e conclusões sobre desempenho e eficiência energética.

### 🤖 Módulo 4 — Relatórios Inteligentes com IA
- **Integração com Google Gemini** (API Generative AI).  
- Botões para:
  - **Gerar Relatório Técnico de Status**
  - **Gerar Lições Aprendidas**
- Textos formatados automaticamente em estilo profissional.
- Opção para download dos dados em `.csv`.

---

## 🧱 Estrutura de Pastas
```
bakery-manager/
│
├── config/
│   ├── .gitignore
│   └── requirements.txt
│
├── app.py                      # Aplicação Flask principal
│
├── data/
│   └── iot_data.csv            # Dados simulados dos sensores
│
├── static/
│   ├── css/                    # Estilos e layout
│   └── js/                     # Scripts JS (gráficos, IA, histórico)
│
└── templates/
    ├── base.html               # Layout principal
    ├── iot.html                # Monitoramento IoT
    ├── insights.html           # KPIs e análises
    ├── relatorios.html         # Relatórios com IA
    ├── historico.html          # Dados históricos
    └── sprints.html            # Documentação de progresso
```
---

### 🧩 Tecnologias Utilizadas
- Python 3.12+
- Flask
- Pandas
- Chart.js
- HTML5 / CSS3 / JavaScript
- Google Gemini API
- dotenv

---
💡Exemplos de Insights Gerados
- “Após a instalação dos sensores de presença, observou-se uma redução média de 15% no consumo de energia.”

- “A temperatura média dos fornos se manteve estável em 195°C, indicando bom controle térmico e eficiência energética.”
---
 
## ⚙️ Como Executar Localmente

1. **Clone o repositório**
   ```bash
   git clone https://github.com/Arruda-007/Bakery-Manager.git
   ```
2. **Acesse a pasta do projeto**
   ```bash
   cd Bakery-Manager
   ```
3. **Crie e ative o ambiente virtual (opcional)**
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Linux/Mac
   ```
4. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```
5. **Configure sua chave da API Gemini**
   Crie um arquivo .env na raiz do projeto:
   ```bash
   GEMINI_API_KEY=AIzaSyDsHrSlZnEDw3qKfpvKmwVVhLth82MsYi8
   ```   
6. **Execute o servidor Flask**
   ```bash
   python app.py
   ```
7. **Acesse no navegador**
   ```bash
   http://127.0.0.1:5000/
   ```
---

👨‍💻 Autor: Cauê Arruda
📍 Rio de Janeiro, Brasil
🎓 Desenvolvedor Back-end
