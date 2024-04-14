<template>
  <div :class="['w-full bg-[#131313]', { 'overflow-hidden': !isExtended }]" :style="{ height: isExtended ? 'auto' : currentHeight }">
    <h1 class="uppercase text-white text-center font-[600] text-2xl w-full md:text-4xl lg:text-5xl xl:text-6xl pt-28 pb-10 reveal-h1">recently added cars</h1>
    <div class="py-20 flex justify-evenly w-full">
      <div class="grid xl:grid-cols-4 lg:grid-cols-3 md:grid-cols-2 sm:grid-cols-2 gap-x-16 gap-y-20">
        <div v-for="(car, index) in cars" :key="index" class="max-w-[280px] h-[350px] z-1 w-full flex flex-col justify-start bg-[#E6E6E6] rounded-xl reveal-car">
          <img :src="car.image" class="w-full h-[50%] rounded-t-xl transition-transform transform hover:scale-105 cursor-pointer" alt="">
          <span class="uppercase text-[10px] mt-2 ml-2 mb-2">{{ car.location }}</span>
          <span class="whitespace-nowrap overflow-hidden overflow-ellipsis cursor-pointer ml-2 uppercase text-lg text-gray-900 hover:text-red-900 font-semibold">{{ car.title }} - {{ car.year }}</span>
          <span class="uppercase font-bold mt-4 ml-2 text-gray-900">{{ car.price }}</span>
          <hr class="h-px mt-7 bg-black border-0">
          <div class="flex flex-row mt-2 ml-2">
            <span class="uppercase text-[10px] p-2 bg-black text-white rounded-full px-3">{{ car.type }}</span>
            <span class="uppercase text-[10px] p-2 bg-black text-white rounded-full px-3 ml-2">{{ car.petrol }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="flex justify-center w-full">
    <button v-if="showButton" @click="toggleHeight" class="mb-20 mt-2 py-3 px-5 flex justify-center items-center rounded-xl bg-black text-white">
      <span>{{ isExtended ? 'SEE LESS' : 'SEE MORE' }}</span>
      <div class="pointer-events-none ml-2 select-none flex items-center">
          <ChevronDownIcon
            class="w-4 h-4 pointer-events-none transition-transform ease-in duration-300 absolute"
            :class="{ 'rotate-180 opacity-0': isExtended, 'rotate-0 opacity-100': !isExtended }"
          />
          <ChevronUpIcon
            class="w-4 h-4 pointer-events-none transition-transform ease-in duration-300"
            :class="{ 'rotate-180 opacity-0': !isExtended, 'rotate-0 opacity-100': isExtended }"
          />
      </div>
    </button>
  </div>
</template>

<script>
import { ChevronDownIcon, ChevronUpIcon } from '@heroicons/vue/24/solid'
export default {
  data() {
    return {
      cars: [
        { title: 'Bmw f90', year: 2015, location: 'Tbilisi',  image: '/peakpx.jpg', owner: 'Vaanskii', price: 5000+ ' $', type: 'SEDAN', petrol: 'Gasoline'},
        { title: 'Card 1', year: 2024, image: '/peakpx.jpg', location: 'Tbilisi', owner: 'Toka', price: 5000+ ' $', type: 'SUV', petrol: 'Gasoline'},
        { title: 'Card 2', year: 2001, image: '/mercedes.jpg', location: 'Tbilisi', owner: 'Luka', price: 5000+ ' $', type: 'SEDAN', petrol: 'Diesel'},
        { title: 'Card 4', year: 2015, image: '/mercedes.jpg', location: 'Tbilisi', owner: 'Nika', price: 5000+ ' $', type: 'SPORT', petrol: 'Gasoline'},
        { title: 'Card 5', year: 2010, image: '/peakpx.jpg', location: 'Tbilisi', owner: 'Vaanskii', price: 5000+ ' $', type: 'SUV', petrol: 'Diesel'},
        { title: 'Card 6', year: 2020, image: '/mercedes.jpg', location: 'Tbilisi', owner: 'Zura', price: 5000+ ' $', type: 'SUV', petrol: 'Gasoline'},
        { title: 'Card 5', year: 2019, image: '/peakpx.jpg', location: 'Tbilisi', owner: 'Vaanskii', price: 5000+ ' $', type: 'SEDAN', petrol: 'Diesel'},
        { title: 'Card 6', year: 2000, image: '/mercedes.jpg', location: 'Tbilisi', owner: 'Zura', price: 5000+ ' $', type: 'SUV', petrol: 'Gasoline'},
        { title: 'Card 6', year: 2000, image: '/mercedes.jpg', location: 'Tbilisi', owner: 'Zura', price: 5000+ ' $', type: 'SUV', petrol: 'Gasoline'},
      ],
      isExtended: false,
      currentHeight: '1200px',
      windowWidth: window.innerWidth
    };
  },
  mounted() {
    this.revealContentOnScroll();
    window.addEventListener('resize', this.updateButtonVisibility);
    this.updateButtonVisibility(); // Initial check on load
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.updateButtonVisibility);
  },
  computed: {
    showButton() {
      const width = this.windowWidth;
      if (width >= 1280 && this.cars.length > 8) return true;
      if (width < 1280 && width >= 1024 && this.cars.length > 6) return true;
      if (width < 1024 && width >= 768 && this.cars.length > 4) return true;
      if (width < 768 && this.cars.length > 2) return true;
      return false;
    }
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
    },
    toggleHeight() {
      this.isExtended = !this.isExtended;
      this.currentHeight = this.isExtended ? 'auto' : '1200px';
      if (!this.isExtended) {
        window.scrollTo({
          top: this.$el.offsetTop,
          behavior: 'smooth'
        });
      }
    },
    updateButtonVisibility() {
      this.windowWidth = window.innerWidth;
    }
  },
  components: {
    ChevronDownIcon, 
    ChevronUpIcon
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
