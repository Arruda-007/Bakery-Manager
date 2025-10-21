// ===== BURNDOWN CHART =====
const ctx = document.getElementById('burndownChart');

if (ctx) {
  new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['Semana 1', 'Semana 2', 'Semana 3', 'Semana 4', 'Semana 5', 'Semana 6'],
      datasets: [
        {
          label: 'Tarefas Planejadas',
          data: [20, 16, 12, 8, 4, 0],
          borderColor: '#bacca4',
          borderWidth: 2,
          fill: false,
          tension: 0.3
        },
        {
          label: 'Tarefas Restantes',
          data: [20, 18, 15, 12, 6, 2],
          borderColor: '#018790',
          borderWidth: 3,
          fill: false,
          tension: 0.3
        }
      ]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          labels: { color: '#fff' }
        },
        title: {
          display: false
        }
      },
      scales: {
        x: {
          ticks: { color: '#fff' },
          grid: {
             color: 'rgba(255,255,255,0.08)', // linhas suaves e visíveis
             borderDash: [2, 2] // deixa pontilhado leve (opcional)
            }
        },
        y: {
          ticks: { color: '#fff' },
          grid: {
             color: 'rgba(255,255,255,0.08)', // linhas suaves e visíveis
             borderDash: [2, 2] // deixa pontilhado leve (opcional)
            }
        }
      }
    }
  });
}

// ======== MODULO 2 ========
// ======== FUNÇÃO GENÉRICA DE OPÇÕES ========
function chartOptions() {
  return {
    responsive: true,
    scales: {
      x: {
        ticks: { color: '#fff' },
        grid: { color: 'rgba(255,255,255,0.08)', borderDash: [2, 2] }
      },
      y: {
        ticks: { color: '#fff' },
        grid: { color: 'rgba(255,255,255,0.08)', borderDash: [2, 2] }
      }
    },
    plugins: { legend: { labels: { color: '#fff' } } }
  };
}

// ======== SIMULAÇÃO DE SENSORES IOT ========
function randomValue(min, max) {
  return (Math.random() * (max - min) + min).toFixed(1);
}

const timeLabels = [];
const maxPoints = 10;

const sensors = {
  temp: { label: 'Temperatura (°C)', color: '#7dad93', range: [170, 220] },
  energy: { label: 'Energia (kWh)', color: '#018790', range: [25, 40] },
  occup: { label: 'Ocupação (%)', color: '#bacca4', range: [30, 95] },
  humidity: { label: 'Umidade (%)', color: '#0a516d', range: [40, 85] },
  gas: { label: 'Gás (ppm)', color: '#ff6b6b', range: [0, 300] },
  smoke: { label: 'Fumaça (ppm)', color: '#f1a208', range: [0, 200] },
  light: { label: 'Luminosidade (lux)', color: '#f9dc5c', range: [100, 800] },
  water: { label: 'Fluxo de Água (L/min)', color: '#5dade2', range: [5, 25] },
  level: { label: 'Nível (%)', color: '#7dd87d', range: [50, 100] },
  motion: { label: 'Movimento (on/off)', color: '#a29bfe', range: [0, 1] }
};

// Inicializa gráficos dinamicamente
const charts = {};
for (const [key, s] of Object.entries(sensors)) {
  const ctx = document.getElementById(`${key}Chart`);
  if (ctx) {
    charts[key] = new Chart(ctx, {
      type: 'line',
      data: {
        labels: [],
        datasets: [{
          label: s.label,
          data: [],
          borderColor: s.color,
          borderWidth: 2,
          fill: false,
          tension: 0.4
        }]
      },
      options: chartOptions()
    });
  }
}

// Atualiza os sensores
setInterval(() => {
  const now = new Date().toLocaleTimeString().split(' ')[0];

  for (const [key, s] of Object.entries(sensors)) {
    const value = randomValue(s.range[0], s.range[1]);
    const chart = charts[key];
    if (!chart) continue;

    if (chart.data.labels.length >= maxPoints) {
      chart.data.labels.shift();
      chart.data.datasets[0].data.shift();
    }

    chart.data.labels.push(now);
    chart.data.datasets[0].data.push(value);
    chart.update();

    // Atualiza valores principais
    if (key === 'temp') document.getElementById('tempValue').textContent = `${value} °C`;
    if (key === 'energy') document.getElementById('energyValue').textContent = `${value} kWh`;
    if (key === 'occup') document.getElementById('occupValue').textContent = `${value}%`;
  }
},10000); // Atualiza a cada 10 segundos
