const observador = new IntersectionObserver((entradas) => {
    entradas.forEach(entrada => {
        if (entrada.isIntersecting) {
            entrada.target.classList.add('visible');
        }
    });
}, {
    threshold: 0.1
});

document.querySelectorAll('section, section ul li, #contacto p').forEach(el => {
    el.classList.add('animar');
    observador.observe(el);
});

function mostrarProyectos() {
  const intro = document.getElementById("intro");
  const proyectos = document.getElementById("proyectos");

  intro.classList.add("hide-intro");

  setTimeout(() => {
    intro.style.display = "none";
    proyectos.style.display = "block";
  }, 800); // coincide con duración de fadeSlideOut
}


document.querySelectorAll('.dropdown-btn').forEach(button => {
    button.addEventListener('click', () => {
        button.classList.toggle('open');
    });
});
