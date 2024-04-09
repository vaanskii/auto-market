<template>
    <div class="w-full bg-black">
      <h1 class="uppercase text-white text-center text-6xl pt-28 pb-10 reveal-h1">recently added cars</h1>
      <div class="mb-40 py-20 flex justify-center">
        <div class="grid grid-cols-3 gap-x-56 gap-y-20">
          <div v-for="(image, index) in images" :key="index" class="w-72 h-96 cursor-pointer bg-[#E6E6E6] flex items-start justify-center rounded-xl reveal-car">
            <img :src="`/${image}`" class="w-[99%] h-[50%] mt-1 rounded-t-xl transition-transform transform hover:scale-105" alt="">
          </div>
        </div>
      </div>
    </div>
</template>
  
  <script>
  export default {
    data() {
      return {
        images: [
          'background.jpg',
          'mercedes.jpg',
          'mercedes.jpg',
          'mercedes.jpg',
          'mercedes.jpg',
          'mercedes.jpg',
        ]
      };
    },
    mounted() {
      this.revealContentOnScroll();
    },
    methods: {
      revealContentOnScroll() {
        window.addEventListener('scroll', () => {
          const revealElements = document.querySelectorAll('.reveal-h1, .reveal-car');
          const windowHeight = window.innerHeight;
          
          revealElements.forEach(el => {
            const elementTop = el.getBoundingClientRect().top;
            const revealPoint = 150;
            
            if (elementTop < windowHeight - revealPoint) {
              el.classList.add('active');
            } else {
              el.classList.remove('active');
            }
          });
        });
      }
    }
  }
  </script>
  
  <style scoped>
  .reveal-h1, .reveal-car {
    opacity: 0;
    transform: translateY(180px);
    transition: opacity 0.5s ease, transform 2s ease;
  }
  
  .reveal-h1.active, .reveal-car.active {
    opacity: 1;
    transform: translateY(0);
  }
  </style>
  