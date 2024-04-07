<template>
  <vue-horizontal responsive class="md:w-full overflow-hidden">
    <section v-for="(card, index) in cards" :key="card.title" class="group sm:w-1/2 md:w-1/3 lg:w-1/4 w-[90%]">
      <div class="relative">
        <img class="md:w-full w-[100%] cursor-pointer max-w-full md:h-60 h-52 transition-transform transform hover:scale-105 rounded-md" :src="card.image" alt="">
      </div>
      <h3 class="cursor-pointer">{{ card.title }}</h3>
      <p class="cursor-pointer">{{ card.price }}</p>
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
        { title: 'iyideba bmw f90',  image: '/peakpx.jpg', owner: 'Vaanskii', price: 5000+ '$'},
        { title: 'Card 2',  image: '/mercedes.jpg', owner: 'Luka', price: 5000+ '$'},
        { title: 'Card 3',  image: '/peakpx.jpg', owner: 'Toka', price: 5000+ '$'},
        { title: 'Card 4',  image: '/mercedes.jpg', owner: 'Nika', price: 5000+ '$'},
        { title: 'Card 5',  image: '/peakpx.jpg', owner: 'Vaanskii', price: 5000+ '$'},
        { title: 'Card 6',  image: '/mercedes.jpg', owner: 'Zura', price: 5000+ '$'},
        { title: 'Card 5',  image: '/peakpx.jpg', owner: 'Vaanskii', price: 5000+ '$'},
        { title: 'Card 6',  image: '/mercedes.jpg', owner: 'Zura', price: 5000+ '$'},
        { title: 'Card 6',  image: '/mercedes.jpg', owner: 'Zura', price: 5000+ '$'},
      ],
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
</style>
