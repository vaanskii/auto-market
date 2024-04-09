<template>
  <vue-horizontal responsive class="md:w-full overflow-hidden">
    <section v-for="(card, index) in cards" :key="card.title" class="group sm:w-1/2 md:w-1/3 lg:w-1/4 w-[90%] reveal-card">
      <div class="relative">
        <img class="md:w-full w-[100%] cursor-pointer max-w-full md:h-60 h-52 transition-transform transform hover:scale-105 rounded-t-md" :src="card.image" alt="">
      </div>
      <div class="bg-[#E6E6E6] text-black shadow-sm mt-1 rounded-b-lg flex justify-center flex-col items-start cursor-pointer transition-transform transform hover:scale-105">
        <h3 class="uppercase ml-4 cursor-pointer max-w-[90%] whitespace-nowrap overflow-hidden overflow-ellipsis">{{ card.title }}</h3>
        <p class="cursor-pointer ml-4 mt-3 mb-2">{{ card.price }}</p>
      </div>
    </section>
  </vue-horizontal>
</template>

<script>
import VueHorizontal from "vue-horizontal";
export default {
  components: { VueHorizontal },
  data() {
    return {
      cards: [
        { title: 'iyideba bmw f90 2024 wliani fcdsfdsfsdf',  image: '/peakpx.jpg', owner: 'Vaanskii', price: 5000+ '$'},
        { title: 'Card 1',  image: '/peakpx.jpg', owner: 'Toka', price: 5000+ '$'},
        { title: 'Card 2',  image: '/mercedes.jpg', owner: 'Luka', price: 5000+ '$'},
        { title: 'Card 4',  image: '/mercedes.jpg', owner: 'Nika', price: 5000+ '$'},
        { title: 'Card 5',  image: '/peakpx.jpg', owner: 'Vaanskii', price: 5000+ '$'},
        { title: 'Card 6',  image: '/mercedes.jpg', owner: 'Zura', price: 5000+ '$'},
        { title: 'Card 5',  image: '/peakpx.jpg', owner: 'Vaanskii', price: 5000+ '$'},
        { title: 'Card 6',  image: '/mercedes.jpg', owner: 'Zura', price: 5000+ '$'},
        { title: 'Card 6',  image: '/mercedes.jpg', owner: 'Zura', price: 5000+ '$'},
      ],
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
  transform: translateX(-100px); /* Change from translateY to translateX */
  transition: opacity 0.5s ease, transform 2s ease;
}

.reveal-card.active {
  opacity: 1;
  transform: translateX(0);
}
</style>
