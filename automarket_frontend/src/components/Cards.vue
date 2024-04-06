<template>
  <vue-horizontal responsive class="md:w-full overflow-hidden">
    <section v-for="(card, index) in cards" :key="card.title" class="group sm:w-1/2 md:w-1/3 lg:w-1/4 w-[90%]">
      <div class="relative">
        <img class="md:w-full w-[100%] max-w-full md:h-60 h-52 transition-transform transform hover:scale-110" :src="card.image" alt="">
        <div class="absolute inset-0 flex items-center justify-center bg-black bg-opacity-25 opacity-0 hover:opacity-100 transition-opacity">
          <button class="text-white uppercase font-semibold py-2 px-4 rounded bg-gray-900 hover:bg-black">View Details</button>
        </div>
      </div>
      <h3>{{ card.title }}</h3>
      <p>{{ card.price }}</p>
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
  background: #f5f5f5;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
</style>
