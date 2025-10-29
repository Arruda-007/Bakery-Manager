const gas = parseInt(document.querySelectorAll(".kpi-value")[4].innerText);
const fumaça = parseInt(document.querySelectorAll(".kpi-value")[5].innerText);

const ctx = document.getElementById("alertChart");

new Chart(ctx, {
  type: "pie",
  data: {
    labels: ["Vazamentos de Gás", "Casos de Fumaça"],
    datasets: [{
      data: [gas, fumaça],
      backgroundColor: ["#ef476f", "#f1a208"],
      borderColor: "#fff",
      borderWidth: 2
    }]
  },
  options: {
    plugins: {
      legend: {
        labels: { color: "#fff" }
      }
    }
  }
});
