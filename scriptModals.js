function abrirModal(id) {
    const modal = document.getElementById(`modal-${id}`);
    if (modal) {
      modal.style.display = 'block';
    }
  }
  
  function cerrarModal(id) {
    const modal = document.getElementById(`modal-${id}`);
    if (modal) {
      modal.style.display = 'none';
    }
  }
  
  // Cierra el modal al hacer clic fuera del contenido
  window.addEventListener('click', (e) => {
    if (e.target.classList.contains('modal')) {
      e.target.style.display = 'none';
    }
  });
  
window.onload = () => {
  // Empieza en la parte inferior
  window.scrollTo(0, document.body.scrollHeight);

  setTimeout(() => {
    const duration = 500; // duración del scroll en ms
    const start = window.pageYOffset;
    const startTime = performance.now();

    // Función de easing para suavizar el scroll
    function easeOutCubic(t) {
      return 1 - Math.pow(1 - t, 3);
    }

    function scrollStep(timestamp) {
      const elapsed = timestamp - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const easedProgress = easeOutCubic(progress);
      window.scrollTo(0, start * (1 - easedProgress));

      if (progress < 1) {
        requestAnimationFrame(scrollStep);
      }
    }

    requestAnimationFrame(scrollStep);
  }, 800);
};
