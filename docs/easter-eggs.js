/* Ativação dos temas secretos ao clicar nos nomes dos autores.
   Clicar novamente no mesmo nome restaura o tema lilás/rosa.
   Clicar no outro nome troca diretamente de tema. */
(() => {
  "use strict";
  const buttons = {
    spider: document.getElementById("theo-theme"),
    music: document.getElementById("giovanna-theme")
  };
  const hint = document.getElementById("theme-hint");
  if (!buttons.spider || !buttons.music) return;
  let current = null;

  function applyTheme(selected) {
    current = current === selected ? null : selected;
    document.body.classList.toggle("theme-spider", current === "spider");
    document.body.classList.toggle("theme-music", current === "music");

    Object.entries(buttons).forEach(([key, button]) => {
      const active = current === key;
      const owner = key === "spider" ? "Theo" : "Giovanna";
      const label = key === "spider" ? "inspirado no Homem-Aranha" : "musical";
      button.setAttribute("aria-pressed", String(active));
      button.setAttribute("aria-label", active
        ? "Desativar tema " + label + " de " + owner
        : "Ativar tema " + label + " de " + owner);
      button.title = active ? "Clique novamente para voltar ao original" : "Clique para ativar o tema secreto";
    });

    if (hint) {
      hint.textContent = current === "spider"
        ? "🕸️ Modo Theo ativado! Clique em Theo novamente para voltar ao tema original."
        : current === "music"
          ? "♫ Modo Giovanna ativado! Clique em Giovanna novamente para voltar ao tema original."
          : "Dica: clique no nome de cada autor para descobrir um tema secreto.";
    }
  }

  buttons.spider.addEventListener("click", () => applyTheme("spider"));
  buttons.music.addEventListener("click", () => applyTheme("music"));
})();
