document.addEventListener("DOMContentLoaded", () => {
  const loading = document.getElementById("loading");
  const resultado = document.getElementById("resultadoTexto");

  async function gerar(endpoint) {
    loading.classList.remove("hidden");
    resultado.innerHTML = "";

    try {
      const res = await fetch(`/api/${endpoint}`);
      const data = await res.json();

      // Converter o texto Markdown em HTML bonito
      resultado.innerHTML = marked.parse(data.relatorio);
    } catch (err) {
      resultado.innerHTML = "<p style='color:red;'>❌ Erro ao gerar relatório.</p>";
    } finally {
      loading.classList.add("hidden");
    }
  }

  document.getElementById("btnStatus").addEventListener("click", () => gerar("gerar_relatorio"));
  document.getElementById("btnLessons").addEventListener("click", () => gerar("licoes_aprendidas"));
});
