document.addEventListener("DOMContentLoaded", () => {
  // ==== 1️⃣ Total de Horas ====
  const totalHoras = 124; // Exemplo — pode ser calculado no futuro
  document.getElementById("totalHoras").textContent = totalHoras + " h";

  // ==== 2️⃣ Gráfico de Linha — Temperatura ====
  const tempCtx = document.getElementById("tempChart");
  new Chart(tempCtx, {
    type: "line",
    data: {
      labels: ["Seg", "Ter", "Qua", "Qui", "Sex"],
      datasets: [{
        label: "Temperatura Média (°C)",
        data: [22, 23.5, 24, 23, 25],
        borderColor: "#018790",
        backgroundColor: "rgba(1, 135, 144, 0.1)",
        borderWidth: 2,
        fill: true,
        tension: 0.3
      }]
    },
    options: {
      responsive: true,
      scales: {
        y: { beginAtZero: false }
      }
    }
  });

  // ==== 3️⃣ Gráfico de Barras — Horas Planejadas x Reais ====
  const horasCtx = document.getElementById("horasChart");
  new Chart(horasCtx, {
    type: "bar",
    data: {
      labels: ["Semana 1", "Semana 2", "Semana 3", "Semana 4"],
      datasets: [
        {
          label: "Horas Planejadas",
          data: [10, 12, 15, 8],
          backgroundColor: "#7dad93"
        },
        {
          label: "Horas Reais",
          data: [12, 11, 17, 9],
          backgroundColor: "#018790"
        }
      ]
    },
    options: {
      responsive: true,
      scales: {
        y: { beginAtZero: true }
      },
      plugins: {
        legend: { position: "top" }
      }
    }
  });
});
