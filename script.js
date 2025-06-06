// ==============================================
// Configuración del Menú Hamburguesa Móvil
// ==============================================

document.addEventListener('DOMContentLoaded', function() {
    // Seleccionar elementos del menú móvil
    const mobileMenuToggle = document.getElementById('mobileMenuToggle');
    const mobileMenuClose = document.getElementById('mobileMenuClose');
    const mobileSidebar = document.getElementById('mobileSidebar');
    
    // Verificar que los elementos existen
    if (!mobileMenuToggle) {
        console.error('Error: No se encontró el botón hamburguesa (mobileMenuToggle)');
        return;
    }
    if (!mobileSidebar) {
        console.error('Error: No se encontró el menú lateral (mobileSidebar)');
        return;
    }
    
    // Función para abrir el menú
    function openMobileMenu() {
        mobileSidebar.classList.add('active');
        document.body.style.overflow = 'hidden'; // Bloquear scroll
        console.log('Menú abierto');
    }
    
    // Función para cerrar el menú
    function closeMobileMenu() {
        mobileSidebar.classList.remove('active');
        document.body.style.overflow = ''; // Restaurar scroll
        console.log('Menú cerrado');
    }
    
    // Evento para abrir/cerrar menú
    mobileMenuToggle.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        
        if (mobileSidebar.classList.contains('active')) {
            closeMobileMenu();
        } else {
            openMobileMenu();
        }
    });
    
    // Evento para cerrar menú con el botón de cerrar
    if (mobileMenuClose) {
        mobileMenuClose.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            closeMobileMenu();
        });
    }
    
    // Cerrar menú al hacer clic fuera
    document.addEventListener('click', function(e) {
        if (!mobileSidebar.contains(e.target) && e.target !== mobileMenuToggle) {
            closeMobileMenu();
        }
    });
    
    // Cerrar menú con tecla Escape
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && mobileSidebar.classList.contains('active')) {
            closeMobileMenu();
        }
    });
    
    // Prevenir cierre al hacer clic dentro del menú
    mobileSidebar.addEventListener('click', function(e) {
        e.stopPropagation();
    });
    
    console.log('Menú móvil configurado correctamente');
});

// ==============================================
// Configuración del Menú de Escritorio (si es necesario)
// ==============================================

document.addEventListener('DOMContentLoaded', function() {
    const desktopNav = document.querySelector('.desktop-nav');
    
    if (desktopNav) {
        console.log('Menú de escritorio detectado');
        // Aquí puedes agregar cualquier funcionalidad específica para el menú de escritorio
    }
});

// ==============================================
// Compatibilidad con otros scripts
// ==============================================

// Asegurar que no haya conflictos con otros event listeners
function safeAddEventListener(element, event, handler) {
    if (element && typeof handler === 'function') {
        element.addEventListener(event, handler);
        return true;
    }
    return false;
}

// Inicialización segura de todos los componentes
function initializeAll() {
    // Aquí puedes inicializar otros componentes de tu página
    // asegurándote de que no interfieran con el menú móvil
}

// Ejecutar cuando el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', function() {
    initializeAll();
});


// Idiomas
let isTranslated = false;
const originalTexts = new Map();

// Recorrer solo nodos de texto visibles, dentro de los tags que quieres
function getTextNodes() {
  const elements = document.querySelectorAll('h1,h2,h3,p,a,button,li,span');
  const textNodes = [];
  elements.forEach(el => {
    el.childNodes.forEach(node => {
      if (node.nodeType === Node.TEXT_NODE && node.textContent.trim().length > 0) {
        textNodes.push(node);
      }
    });
  });
  return textNodes;
}

// Traduce un texto plano con reglas personalizadas
async function translateText(text, targetLang = 'en') {
  const trimmed = text.trim();

  // Traducción manual para "start"
  if (trimmed.toLowerCase() === 'start') return text.replace(/start/i, 'inicio');

  // Evitar traducir textos exactos o nombres propios
  if (trimmed === 'os') return text;
  if (trimmed === 'Belén') return text;
  if (trimmed === 'Hey Tú - Sombras de Neón') return text;
  if (trimmed === 'Hey Tú') return text;
  if (trimmed === 'Libre Al Fin - Sombras de Neón') return text;
  if (trimmed === 'Libre Al Fin') return text;
  if (trimmed === 'Best-Brands') return text;
  if (trimmed === 'Sombras de Neón') return text;
  if (trimmed.includes('Joshua Saborio')) return text;
  if (trimmed.includes('Tic Tac Toe Web')) return text;

  // Traducciones personalizadas
  if (trimmed.includes('Inicio')) return 'Home';
  if (trimmed.includes('Videos Cinemáticos')) return 'Cinematic Videos';
  if (trimmed.includes('Orden y Aseo')) return 'Order and Hygiene';
  if (trimmed.includes('Diseño Corporativo - BestBrands - 2024/Actualidad')) return 'Corporate Design - BestBrands - 2024/Present';
  if (trimmed.includes('Técnico en Desarrollo de Aplicaciones Móviles (2023 - Actualidad)')) return 'Mobile Application Development Technician (2023 - Present)';
  if (trimmed.includes('Gimnasio')) return 'Gym';
  if (trimmed.includes('Proyecto Ciencias Seres Vivos')) return 'Science Project';
  if (trimmed.includes('Necesita Agua la Planta')) return 'The plant needs water?';
  if (trimmed.includes('App Cálculo de Promedio Y Validación')) return 'App that Calculates Average and Validation';


  // Evitar traducir textos demasiado cortos o vacíos
  if (trimmed.length < 2) return text;

  const url = `https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl=${targetLang}&dt=t&q=${encodeURIComponent(trimmed)}`;
  try {
    const response = await fetch(url);
    const data = await response.json();
    const translated = data[0].map(item => item[0]).join('');
    return text.replace(trimmed, translated);
  } catch (e) {
    console.error('Error al traducir:', e);
    return text;
  }
}

// Traduce todos los textos visibles
async function translateAll() {
  const textNodes = getTextNodes();
  for (const node of textNodes) {
    if (!originalTexts.has(node)) {
      originalTexts.set(node, node.textContent);
    }
  }
  for (const node of textNodes) {
    const original = originalTexts.get(node);
    const translated = await translateText(original, 'en');
    node.textContent = translated;
  }
}

// Revertir traducción
function revertTranslation() {
  for (const [node, text] of originalTexts.entries()) {
    node.textContent = text;
  }
}

// Crear botón de toggle idioma
function createToggleButton() {
  const btn = document.createElement('button');
  btn.textContent = 'EN';
  btn.style.position = 'fixed';
  btn.style.bottom = '20px';
  btn.style.right = '20px';
  btn.style.padding = '10px 14px';
  btn.style.borderRadius = '8px';
  btn.style.backgroundColor = '#007bff'; // Color azul
  btn.style.border = 'none';
  btn.style.cursor = 'pointer';
  btn.style.color = 'white';
  btn.style.zIndex = 9999;
  btn.style.fontSize = '14px';
  btn.style.boxShadow = '0 10px 20px rgba(0, 0, 0, 0.5)';
  btn.style.transition = 'background-color 0.3s, transform 0.2s';
  btn.style.transform = 'scale(1)';
  btn.style.fontWeight = 'bold';
  
  btn.style.fontFamily = 'Arial, sans-serif';

  btn.addEventListener('mouseover', () => {
    btn.style.backgroundColor = '#0056b3'; // Color azul más oscuro al pasar el mouse
    btn.style.transform = 'scale(1.05)'; // Aumenta ligeramente el tamaño
  });

  btn.addEventListener('mouseout', () => {
    btn.style.backgroundColor = '#007bff'; // Vuelve al color original
    btn.style.transform = 'scale(1)'; // Vuelve al tamaño original
  }
  );

  btn.addEventListener('click', async () => {
    btn.disabled = true;
    btn.textContent = '...';
    if (!isTranslated) {
      await translateAll();
      btn.textContent = 'ES';
      isTranslated = true;
    } else {
      revertTranslation();
      btn.textContent = 'EN';
      isTranslated = false;
    }
    btn.disabled = false;
  });

  document.body.appendChild(btn);
}

document.addEventListener('DOMContentLoaded', () => {
  createToggleButton();
});

 

function mostrarProyectos() {
  const intro = document.getElementById("intro");
  const proyectos = document.getElementById("proyectos");

  intro.classList.add("hide-intro");

  setTimeout(() => {
    // Aquí redirigimos a proyectos.html
    window.location.href = "proyectos.html";
  }, 800); // espera la duración de la animación antes de cambiar de página
}

window.addEventListener("DOMContentLoaded", (event) => {
  const audio = document.getElementById("entradaAudio");
  audio.volume = 0.1; // Ajusta el volumen del audio
  audio.play(); // Reproduce el sonido al cargar la página
});


// Fondo de Burbujas Interactivas

document.addEventListener("DOMContentLoaded", () => {
  const interBubble = document.querySelector(".interactive");
  let curX = 0;
  let curY = 0;
  let tgX = 0;
  let tgY = 0;

  function move() {
    curX += (tgX - curX) / 5;
    curY += (tgY - curY) / 5;
    interBubble.style.left = `${curX}px`;
    interBubble.style.top = `${curY}px`;
    requestAnimationFrame(move);
  }

  window.addEventListener("mousemove", (event) => {
    tgX = event.clientX;
    tgY = event.clientY;
  });

  move();
});

// Seleccionar sección

document.addEventListener("DOMContentLoaded", function () {
  const buttons = document.querySelectorAll(".nav-btn");
  const sections = document.querySelectorAll(".section");

  buttons.forEach((button) => {
    button.addEventListener("click", function () {
      const sectionToShow = this.dataset.section;

      sections.forEach((section) => {
        if (section.id === sectionToShow) {
          section.classList.add("active");
        } else {
          section.classList.remove("active");
        }
      });
    });
  });
});

// Carrusel de Proyectos

const items = document.querySelectorAll(".carousel-item");
let currentIndex = 0;
let carouselInterval = setInterval(nextItem, 4500); // Inicia el intervalo

function updateCarousel() {
  items.forEach((item, index) => {
    item.classList.remove("active", "prev", "next");
    if (index === currentIndex) {
      item.classList.add("active");
    } else if (index === (currentIndex - 1 + items.length) % items.length) {
      item.classList.add("prev");
    } else if (index === (currentIndex + 1) % items.length) {
      item.classList.add("next");
    }
  });
}

// Funciones para avanzar y volver en el carrusel

function nextItem() {
  currentIndex = (currentIndex + 1) % items.length;
  updateCarousel();
}

function prevItem() {
  currentIndex = (currentIndex - 1 + items.length) % items.length;
  updateCarousel();
}

// Funciones para pausar el carrusel

function pauseCarousel() {
  clearInterval(carouselInterval);
}

// Reanuda el carrusel después de un tiempo

function resumeCarousel() {
  carouselInterval = setInterval(nextItem, 4000);
}

// Agrega eventos de hover al elemento activo
items.forEach((item) => {
  item.addEventListener("mouseenter", () => {
    if (item.classList.contains("active")) {
      pauseCarousel(); // Pausa el carrusel si es el elemento activo
    }
  });

  item.addEventListener("mouseleave", () => {
    if (item.classList.contains("active")) {
      resumeCarousel(); // Reanuda el carrusel al salir del hover
    }
  });
});

// Inicializa el carrusel
updateCarousel();

// Selecciona las flechas
const leftArrow = document.querySelector(".left-arrow");
const rightArrow = document.querySelector(".right-arrow");

// Agrega eventos a las flechas
leftArrow.addEventListener("click", () => {
  pauseCarousel(); // Pausa el carrusel al usar las flechas
  prevItem();
  resumeCarousel(); // Reinicia el casrrusel después de usar las flechas
});

rightArrow.addEventListener("click", () => {
  pauseCarousel(); // Pausa el carrusel al usar las flechas
  nextItem();
  resumeCarousel(); // Reinicia el carrusel después de usar las flechas
});

// Sección de Contacto mediante boton que lleve a whatsapp
function contacto() {
  const correo = "joshua.saborio.contacto@gmail.com";
  const asunto = "Interesado en trabajar contigo";
  const cuerpo = "Hola Joshua, me gustaría contactarte para trabajar contigo.";
  const mailtoLink = `mailto:${correo}?subject=${encodeURIComponent(asunto)}&body=${encodeURIComponent(cuerpo)}`;
  window.location.href = mailtoLink;
}


// Mouse efecto
let sparklesEnabled = true;
let lastSparkleTime = 0;
const sparkleCooldown = 20; // Tiempo mínimo entre brillitos en milisegundos

document.addEventListener('mousemove', (e) => {
  if (!sparklesEnabled) return;

  const now = Date.now();
  if (now - lastSparkleTime < sparkleCooldown) return;
  lastSparkleTime = now;

  const sparkle = document.createElement('div');
  sparkle.classList.add('sparkle');
  sparkle.style.left = `${e.clientX}px`;
  sparkle.style.top = `${e.clientY}px`;

  document.body.appendChild(sparkle);

  setTimeout(() => {
    sparkle.remove();
  }, 1000);
});

document.getElementById('toggleSparkles').addEventListener('click', () => {
  sparklesEnabled = false;
});
