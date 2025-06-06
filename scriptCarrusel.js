document.addEventListener("DOMContentLoaded", () => {
  const track = document.querySelector(".custom-carousel-track");
  const slides = Array.from(track.children);
  const prevBtn = document.querySelector(".custom-carousel-prev");
  const nextBtn = document.querySelector(".custom-carousel-next");
  const lightbox = document.querySelector(".custom-lightbox");
  const lightboxImg = lightbox.querySelector("img");
  const lightboxClose = lightbox.querySelector(".custom-lightbox-close");

  let currentIndex = 0;

  // Set slide positions horizontally
  const setSlidePositions = () => {
    slides.forEach((slide, index) => {
      slide.style.left = `${index * 100}%`;
    });
  };

  setSlidePositions();

  const moveToSlide = (index) => {
    if (index < 0) index = slides.length - 1;
    if (index >= slides.length) index = 0;
    track.style.transform = `translateX(-${index * 100}%)`;
    currentIndex = index;
  };

  prevBtn.addEventListener("click", () => {
    moveToSlide(currentIndex - 1);
  });

  nextBtn.addEventListener("click", () => {
    moveToSlide(currentIndex + 1);
  });

  // Click on slide to open lightbox
  slides.forEach((slide) => {
    slide.addEventListener("click", () => {
      lightbox.style.display = "flex";
      lightboxImg.src = slide.src;
      lightboxImg.alt = slide.alt;
    });
  });

  // Close lightbox
  lightboxClose.addEventListener("click", () => {
    lightbox.style.display = "none";
  });

  // Also close lightbox clicking outside image
  lightbox.addEventListener("click", (e) => {
    if (e.target === lightbox) {
      lightbox.style.display = "none";
    }
  });

  // Initialize position
  moveToSlide(0);
});
