<template>
  <vue-horizontal responsive class="md:w-full overflow-hidden">
    <section v-for="(car, index) in similarCars" :key="car.id" class="group sm:w-1/2 md:w-1/3 lg:w-1/4 w-[90%] reveal-card max-w-[370px]" @click="showCarDetails(car)">
      <router-link :to="Trans.i18nRoute({ name: 'cardetail', params: {'id': car.id} })">
      <div class="relative">
        <img :v-if="car.main_image" :src="car.main_image.image_url" class="md:w-full w-[100%] cursor-pointer max-w-full md:h-60 h-52 transition-transform transform hover:scale-105 rounded-t-md" :alt="car.manufacturer">
      </div>
      <div class="bg-[#E6E6E6] text-black shadow-sm mt-1 rounded-b-lg flex justify-center flex-col items-start cursor-pointer transition-transform transform hover:scale-105">
        <h3 class="uppercase ml-4 cursor-pointer max-w-[90%] whitespace-nowrap overflow-hidden overflow-ellipsis">{{ car.manufacturer }} {{ car.car_model }} - <span class="text-gray-600">{{ car.year }}</span></h3>
        <p class="cursor-pointer ml-4 mt-3 mb-2">{{ car.price }}</p>
      </div>
      </router-link>
    </section>
  </vue-horizontal>
</template>

<script>
import VueHorizontal from "vue-horizontal";
import Trans from "@/i18n/translation";
import { RouterLink } from "vue-router";
export default {
  components: { 
    VueHorizontal, 
    RouterLink
  },
  props: {
    similarCars: {
      type: Array,
      required: true
    }
  },
  setup() {
    return {
      Trans
    }
  },
  data() {
    return {
      cards: [],
    }
  },
  mounted() {
    this.revealCardsOnScroll();
  },
  methods: {
    revealCardsOnScroll() {
      window.addEventListener('scroll', () => {
        const cards = document.querySelectorAll('.reveal-card');
        const windowHeight = window.innerHeight;
        
        cards.forEach(card => {
          const cardTop = card.getBoundingClientRect().top;
          const revealPoint = 150;
          
          if (cardTop < windowHeight - revealPoint) {
            card.classList.add('active');
          } else {
            card.classList.remove('active');
          }
        });
      });
    },
    showCarDetails(car) {
      this.$emit('showCarDetails', car);
      window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
    }
  }
}
</script>

<style scoped>
section {
  padding:5px;
  background: transparent;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.reveal-card {
  opacity: 0;
  transform: translateX(-300px);
  transition: opacity 0.5s ease, transform 2s ease;
}

.reveal-card.active {
  opacity: 1;
  transform: translateX(0);
}
</style>
