
// Modals
(function() {
  const modalScoping = document.getElementById("modalScoping");
  const modalBrief = document.getElementById("modalBrief");
  const btnScoping = document.getElementById("btnScoping");
  const btnBrief = document.getElementById("btnBrief");

  function open(modal) { modal.classList.add("open"); }
  function close(modal) { modal.classList.remove("open"); }

  btnScoping && btnScoping.addEventListener("click", () => open(modalScoping));
  btnBrief && btnBrief.addEventListener("click", () => open(modalBrief));

  document.querySelectorAll("[data-close]").forEach(btn => {
    btn.addEventListener("click", () => close(btn.closest(".modal")));
  });
  
})();