// Simple slider
(function() {
  const slides = document.querySelectorAll(".slide");
  const prev = document.querySelector(".slider .prev");
  const next = document.querySelector(".slider .next");
  let idx = 0;
  function show(i) {
    slides.forEach((s, n) => s.classList.toggle("active", n === i));
  }
  function advance(step = 1) {
    idx = (idx + step + slides.length) % slides.length;
    show(idx);
  }
  show(idx);
  let timer = setInterval(() => advance(1), 5000);
  [prev, next].forEach(btn => btn && btn.addEventListener("click", (e) => {
    clearInterval(timer);
    advance(btn === next ? 1 : -1);
  }));
})();


// Another simple slider implementation
document.addEventListener('DOMContentLoaded', function() {
    const slides = document.querySelectorAll('.slide');
    const prevBtn = document.querySelector('.prev');
    const nextBtn = document.querySelector('.next');
    let currentIndex = 0;

    function showSlide(index) {
        slides.forEach((slide, i) => {
            slide.style.display = (i === index) ? 'block' : 'none';
        });
    }

    prevBtn.addEventListener('click', () => {
        currentIndex = (currentIndex > 0) ? currentIndex - 1 : slides.length - 1;
        showSlide(currentIndex);
    });

    nextBtn.addEventListener('click', () => {
        currentIndex = (currentIndex < slides.length - 1) ? currentIndex + 1 : 0;
        showSlide(currentIndex);
    });

    showSlide(currentIndex);
});



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
  [modalScoping, modalBrief].forEach(m => {
    m.addEventListener("click", (e) => {
      if (e.target === m) close(m);
    });
  });
})();