# 🧁 Smart Bakery 4.0 — Sistema de Monitoramento IoT  

🚀 **Smart Bakery 4.0** é um sistema desenvolvido em **Flask (Python)** para monitorar, analisar e gerar relatórios sobre dados de uma padaria inteligente, integrando sensores IoT, gráficos interativos e análise de desempenho.  

---

## 📂 Estrutura do Projeto

smart_bakery/ <br>
│ <br>
├── app.py # Aplicação principal Flask <br>
├── data/ <br>
│ └── iot_data.csv # Dados gerados dos sensores Io T<br>
├── templates/ <br>
│ ├── base.html # Layout base <br>
│ ├── index.html # Tela inicial <br>
│ ├── iot.html # Monitoramento em tempo real <br>
│ ├── historico.html # Visualização de dados históricos <br>
│ ├── insights.html # KPIs e gráficos comparativos <br>
│ ├── relatorios.html # Geração de relatórios técnicos <br>
│ └── sprints.html # Tela das sprints do projeto <br>
├── static/ <br>
│ ├── css/ <br>
│ │ └── style.css # Estilos visuais do sistema <br>
│ ├── js/ <br>
│ │ ├── iot.js # Sensores e gráficos em tempo real <br>
│ │ ├── historico.js # Gráficos do histórico real <br>
│ │ └── insights.js # KPIs e comparativos dos sensores <br>
│ └── img/ # Imagens do sistema <br>
└── requirements.txt # Dependências do projeto <br>

---

## ⚙️ Funcionalidades

### 🧠 Módulo IoT
Monitoramento **em tempo real** dos sensores:
- Temperatura  
- Consumo de Energia  
- Umidade  
- Ocupação da Loja  
- Vazamento de Gás  
- Fumaça  
- Luminosidade  
- Fluxo de Água  
- Nível do Reservatório  
- Presença / Movimento  

---

### 📊 Módulo Insights
- Exibição de **KPIs automáticos** (médias por sensor)  
- Gráfico comparativo geral dos sensores  
- Cores e layout personalizados conforme identidade da Smart Bakery  

---

### 📈 Módulo Histórico Real
- Visualização dos dados registrados em **CSV**  
- Gráficos interativos de todas as variáveis  
- Atualização dinâmica com dados reais  

---

### 📝 Módulo Relatórios
- Geração automática de relatórios técnicos com base nos dados históricos  
- Pode usar:
  - **OpenAI GPT-3.5** (caso a chave esteja configurada no `.env`), ou  
  - **Relatório local automático** (sem necessidade de API)  

---

### 📥 Exportação
- Download direto dos dados em formato `.csv`  
- Pronto para integração com **Tableau**, **Power BI** ou outras ferramentas de BI  

---

## 🧰 Tecnologias Utilizadas

| Categoria | Tecnologias |
|------------|--------------|
| Backend | Python, Flask |
| Frontend | HTML5, CSS3, JavaScript, Chart.js |
| Banco de Dados | CSV (simulação de dados IoT) |
| Análise | Pandas |
| API | OpenAI GPT-3.5 |
| Ferramentas | VS Code, GitHub |

---

## 🖥️ Como Executar Localmente

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seuusuario/smart-bakery.git
  ```

2. Acesse a pasta:
    ```
   cd smart-bakery
  ```
4. Crie e ative o ambiente virtual (opcional):
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate  # Linux/Mac
 
5. Instale as dependências:
   pip install -r requirements.txt
    
6. Execute o projeto:
   python app.py

6. Acesse no navegador:
   http://127.0.0.1:5000/
 

🔐 (Opcional) Integração com OpenAI
Se quiser gerar relatórios com inteligência artificial:

Crie um arquivo chamado .env na raiz do projeto.

Adicione sua chave de API da OpenAI:
Copiar código
OPENAI_API_KEY=coloque_sua_chave_aqui

## 📸 Principais Telas
| Tela | Descrição |
|------------|--------------|
| 🏠 Início | Apresentação do sistema Bakery Manager 4.0 |
| ⚙️ Monitoramento IoT | Sensores em tempo real com gráficos dinâmicos |
| 📈 Histórico Real | Análise de dados gravados no CSV |
| 📊 Insights | KPIs e comparativos automáticos |
| 📝 Relatórios | Geração de relatórios técnicos com IA |
| 📅 Sprints | Organização e planejamento do projeto |


✨ Autores <br>
👨‍💻 Desenvolvido por Cauê Arruda e equipe Bakery Manager <br>
📍 Projeto acadêmico — Análise e Desenvolvimento de Sistemas <br>
📚 Rio de Janeiro — 2025

🧠 Licença
Este projeto é de uso acadêmico e livre para estudo, modificação e aprimoramento.
