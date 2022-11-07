<!-- Swiper JS -->
src="https://cdn.jsdelivr.net/npm/swiper/swiper-bundle.min.js"

// <!-- Initialize Swiper -->
var swiper = new Swiper(".mySwiper", {
	spaceBetween:0,
	effect: "fade",
	//centeredSlides: true,
	autoplay: {
	  delay: 2500,
	  disableOnInteraction: false,
	},
	pagination: {
	  el: ".swiper-pagination",
	  clickable: true,
	},
	navigation: {
	  nextEl: ".swiper-button-next",
	  prevEl: ".swiper-button-prev",
	},
  });