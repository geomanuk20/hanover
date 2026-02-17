document.addEventListener("DOMContentLoaded", function () {
  const menuIcon = document.querySelector(".menu-icon");
  const nav = document.getElementById("mainNav");

  menuIcon.addEventListener("click", function () {
    nav.classList.toggle("nav-active");

    // Change icon between bars and times
    const icon = this.querySelector("i");
    if (icon.classList.contains("fa-bars")) {
      icon.classList.remove("fa-bars");
      icon.classList.add("fa-times");
    } else {
      icon.classList.remove("fa-times");
      icon.classList.add("fa-bars");
    }
  });

  // Close menu when clicking on a link (optional)
  const navLinks = document.querySelectorAll(".nav-links a");
  navLinks.forEach((link) => {
    link.addEventListener("click", function () {
      nav.classList.remove("nav-active");
      const icon = document.querySelector(".menu-icon i");
      icon.classList.remove("fa-times");
      icon.classList.add("fa-bars");
    });
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const propertyTypeBtns = document.querySelectorAll(".property-type-btn");

  propertyTypeBtns.forEach((btn) => {
    btn.addEventListener("click", function () {
      // Remove active class from all buttons
      propertyTypeBtns.forEach((b) => b.classList.remove("active"));
      // Add active class to clicked button
      this.classList.add("active");

      // You can store the selected type in a variable or form data
      const selectedType = this.getAttribute("data-type");
      console.log("Selected property type:", selectedType);
    });
  });
});

document.addEventListener("DOMContentLoaded", function () {
  // Initialize both sliders
  initializeSlider("slider1");
  initializeSlider("slider2");

  function initializeSlider(sliderId) {
    const container = document.getElementById(sliderId);
    const slider = container.querySelector(".slider");
    const cards = container.querySelectorAll(".card");
    const prevBtn = container.querySelector(".prev");
    const nextBtn = container.querySelector(".next");

    let currentIndex = 0;
    let cardWidth = cards[0].offsetWidth + 15; // width + gap

    function updateSlider() {
      slider.style.transform = `translateX(-${currentIndex * cardWidth}px)`;
    }

    function getVisibleCards() {
      const containerWidth = container.offsetWidth;
      return Math.floor(containerWidth / cardWidth);
    }

    nextBtn.addEventListener("click", function () {
      const visibleCards = getVisibleCards();
      const maxIndex = Math.max(cards.length - visibleCards, 0);

      if (currentIndex < maxIndex) {
        currentIndex++;
        updateSlider();
      }
    });

    prevBtn.addEventListener("click", function () {
      if (currentIndex > 0) {
        currentIndex--;
        updateSlider();
      }
    });

    // Handle window resize
    window.addEventListener("resize", function () {
      cardWidth = cards[0].offsetWidth + 15;
      updateSlider();
    });
  }
});

document.addEventListener("DOMContentLoaded", function () {
  // Read More functionality
  const readMoreButtons = document.querySelectorAll(".read-more");

  readMoreButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const card = this.closest(".testimonial-card");
      const shortText = card.querySelector(".short");
      const fullText = card.querySelector(".full");

      if (shortText.style.display === "none") {
        shortText.style.display = "-webkit-box";
        fullText.style.display = "none";
        this.textContent = "Read More";
      } else {
        shortText.style.display = "none";
        fullText.style.display = "block";
        this.textContent = "Read Less";
      }
    });
  });

  // Modal functionality
  const modal = document.getElementById("testimonialsModal");
  const viewAllBtn = document.querySelector(".view-all");
  const closeModal = document.querySelector(".close-modal");

  viewAllBtn.addEventListener("click", function () {
    modal.style.display = "block";
    document.body.style.overflow = "hidden";
  });

  closeModal.addEventListener("click", function () {
    modal.style.display = "none";
    document.body.style.overflow = "auto";
  });

  window.addEventListener("click", function (event) {
    if (event.target === modal) {
      modal.style.display = "none";
      document.body.style.overflow = "auto";
    }
  });
});
