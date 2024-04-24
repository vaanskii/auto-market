<template>
  <div :class="['w-full bg-[#131313]', { 'overflow-hidden': !isExtended }]" :style="{ height: currentHeight }" ref="containerRef">
    <h1 class="uppercase text-white text-center font-[600] text-2xl w-full md:text-4xl lg:text-5xl xl:text-6xl pt-28 pb-10 reveal-h1">{{ $t('recently') }}</h1>
    <div class="py-20 flex justify-evenly w-full">
      <div class="grid xl:grid-cols-4 lg:grid-cols-3 md:grid-cols-2 sm:grid-cols-2 gap-x-16 gap-y-20">
        <div v-for="(car, index) in cars" :key="index" class="max-w-[280px] h-[350px] z-1 w-full flex flex-col justify-start bg-[#E6E6E6] rounded-xl reveal-car">
          <img :v-if="car.main_image" :src="car.main_image.image_url" class="w-full h-[50%] rounded-t-xl transition-transform transform hover:scale-105 cursor-pointer" alt="">
          <span class="uppercase text-[10px] mt-2 ml-2 mb-2">{{ car.location }}</span>
          <span class="whitespace-nowrap overflow-hidden overflow-ellipsis cursor-pointer ml-2 uppercase text-lg text-gray-900 hover:text-red-900 font-semibold">{{ car.manufacturer }} - <span class="font-light text-black">{{ car.car_model }}</span></span>
          <span class="uppercase font-bold mt-4 ml-2 text-gray-900">{{ car.price }} <span class="font-semibold">$</span></span>
          <hr class="h-px mt-7 bg-black border-0">
          <div class="flex flex-row mt-2 ml-2">
            <span class="uppercase text-[10px] p-2 bg-black text-white rounded-full px-3">{{ car.created_by.name }}</span>
            <span class="uppercase text-[10px] p-2 bg-black text-white rounded-full px-3 ml-2">{{ car.types }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="flex justify-center w-full">
    <button v-if="showButton" @click="toggleHeight" class="mb-20 mt-2 py-3 px-5 flex justify-center items-center rounded-xl bg-black text-white">
      <span>{{ buttonText }}</span>
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
import axios from 'axios';
import { ChevronDownIcon, ChevronUpIcon } from '@heroicons/vue/24/solid'
import { useI18n } from 'vue-i18n';
import { ref, computed } from 'vue';

export default {
  setup() {
    const { t } = useI18n();
    const isExtended = ref(false); 
    const containerRef = ref(null);

    const buttonText = computed(() => {
      return isExtended.value ? t('seeless') : t('seemore');
    });

    const toggleHeight = () => {
      isExtended.value = !isExtended.value;
      if (!isExtended.value && containerRef.value) {
        window.scrollTo({
          top: containerRef.value.offsetTop,
          behavior: 'smooth'
        });
      }
    };

    return { buttonText, isExtended, toggleHeight, containerRef };
  },
  data() {
    return {
      cars: [],
      windowWidth: window.innerWidth
    };
  },
  mounted() {
    this.getRecentlyAddedCars();
    this.revealContentOnScroll();
    window.addEventListener('resize', this.updateButtonVisibility);
    this.updateButtonVisibility();
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
    },
    currentHeight() {
      if (this.isExtended || this.cars.length <= 4) {
        return 'auto';
      } else {
        return '1200px';
      }
    }
  },
  methods: {
    getRecentlyAddedCars() {
      axios
      .get('/api/recently/')
      .then(response => {
        this.cars = response.data
      })
      .catch(error => {
        console.log(error)
      })
    },
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
  transform: translateY(20px);
  transition: opacity 0.5s, transform 0.5s;
}

.reveal-h1.active, .reveal-car.active {
  opacity: 1;
  transform: translateY(0);
}
</style>
