// insights.js
document.addEventListener("DOMContentLoaded", () => {
  const ctx = document.getElementById("comparativoChart");

  const labels = [
    "Temperatura (°C)",
    "Energia (kWh)",
    "Umidade (%)",
    "Ocupação (%)",
    "Gás (ppm)",
    "Fumaça (ppm)",
    "Luminosidade (lux)",
    "Fluxo de Água (L/min)",
    "Nível (%)",
    "Movimento (%)"
  ];

  // Pega as médias do HTML (convertendo textos em números)
  const valores = Array.from(document.querySelectorAll(".kpi-value")).map(v => parseFloat(v.textContent));

  new Chart(ctx, {
    type: "bar",
    data: {
      labels: labels,
      datasets: [{
        label: "Média dos Sensores",
        data: valores,
        backgroundColor: [
          "#7dad93", "#018790", "#0a516d", "#bacca4",
          "#ff595e", "#f9844a", "#f9dc5c", "#118ab2",
          "#7dd87d", "#ef476f"
        ],
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      scales: {
        y: { beginAtZero: true }
      },
      plugins: {
        legend: { display: false }
      }
    }
  });
});

// ======== GRÁFICO DE CORRELAÇÃO ========
const ctxCorr = document.getElementById("correlationChart");

const labelsCorr = ["Semana 1", "Semana 2", "Semana 3", "Semana 4"];
const antesAutomacao = [120, 115, 130, 128];
const depoisAutomacao = [100, 95, 98, 92];

new Chart(ctxCorr, {
  type: "bar",
  data: {
    labels: labelsCorr,
    datasets: [
      {
        label: "Antes da Automação",
        data: antesAutomacao,
        backgroundColor: "#0a516d"
      },
      {
        label: "Depois da Automação",
        data: depoisAutomacao,
        backgroundColor: "#7dad93"
      }
    ]
  },
  options: {
    responsive: true,
    scales: {
      y: { beginAtZero: true, title: { display: true, text: "Consumo (kWh)" } }
    }
  }
});

// ======== DATA STORYTELLING ========
const reducao = ((antesAutomacao.reduce((a,b)=>a+b) - depoisAutomacao.reduce((a,b)=>a+b))
                 / antesAutomacao.reduce((a,b)=>a+b) * 100).toFixed(1);

document.getElementById("storyText").textContent =
  `Após a automação dos fornos e instalação dos sensores, observou-se uma redução média de ${reducao}% no consumo de energia. ` +
  `Isso indica maior eficiência térmica e menor desperdício de energia, especialmente nos períodos de menor ocupação.`;
