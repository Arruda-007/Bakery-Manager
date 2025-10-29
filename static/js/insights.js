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
