<template>
  <div class="bg-[#E6E6E6] shadow-4xl w-full mt-20">
    <div class="flex justify-center bg-[#E6E6E6] text-center items-center py-10">
      <!-- You can add content here if needed -->
    </div>
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 px-4 lg:px-16 py-8">
      <!-- Blogs -->
      <div class="flex flex-col justify-center items-center bg-[#E6E6E6] shadow-4xl rounded-xl py-8 mb-14 reveal-item">
        <h1 class="uppercase text-5xl font-bold mb-10">{{ $t('blogs.header') }}</h1>
        <img src="/mechanic.png" alt="" class="max-w-full lg:max-w-md rounded-lg">
        <div class="p-6 rounded-lg mt-4">
          <h2 class="text-2xl font-semibold text-center">{{ $t('blogs.question1') }}</h2>
          <p class="mt-4 text-gray-700">{{ $t('blogs.answer1') }}</p>
        </div>
        <router-link :to="Trans.i18nRoute({ name: 'blogs' })">
          <button class="bg-black text-white px-4 py-3 rounded-xl uppercase">{{ $t('blogs.seemore') }}</button>
        </router-link>
      </div>
      <!-- Vin decode -->
      <div class="flex flex-col justify-center items-center bg-[#E6E6E6] shadow-4xl rounded-xl py-8 mb-14 reveal-item">
        <h1 class="uppercase text-3xl font-bold mb-10 text-center">{{ $t('vin.search') }}</h1>
        <div class="w-[90%] max-h-[400px] bg-[#222] rounded-xl">
          <!-- INPUT FIELD -->
          <form class="flex justify-around">
            <div class="w-[90%] h-[400px] flex md:flex-row flex-col items-center md:justify-around justify-center gap-2">
              <input id="vin" type="text" class="w-[90%] bg-[#E6E6E6] py-3 text-xl pl-4 rounded-lg" :placeholder="$t('vin.placeholder')">
              <button type="submit" class="uppercase bg-[#E6E6E6] text-black px-4 py-3.5 rounded-lg w-[90%] md:w-[25%] hover:bg-gray-100">search</button>
            </div>
          </form>
        </div>
        <div class="p-6 rounded-lg mt-4">
          <h2 class="text-2xl font-semibold text-center">{{ $t('vin.understanding') }}</h2>
          <p class="mt-4 text-gray-700">{{ $t('vin.explanation') }}</p>
        </div>
      </div>
    </div>
  </div>
</template>
  
<script>
import { RouterLink } from 'vue-router'
import Trans from '@/i18n/translation'

export default {
  setup() {
    return {
      Trans
    }
  },
  mounted() {
    this.revealItemsOnScroll();
  },
  methods: {
    revealItemsOnScroll() {
      window.addEventListener('scroll', () => {
        const revealItems = document.querySelectorAll('.reveal-item');
        const windowHeight = window.innerHeight;
        
        revealItems.forEach(item => {
          const itemTop = item.getBoundingClientRect().top;
          const revealPoint = 150;
          
          if (itemTop < windowHeight - revealPoint) {
            item.classList.add('active');
          } else {
            item.classList.remove('active');
          }
        });
      });
    }
  }
}
</script>
  
  <style scoped>
  .shadow-4xl {
      --tw-shadow: 0 50px 100px -20px rgba(0, 0, 0, 0.4);
      --tw-shadow-colored: 0 50px 100px -20px var(--tw-shadow-color);
      box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
  }
  
  .reveal-item {
    opacity: 0;
    transform: translateY(80px);
    transition: opacity 0.5s ease, transform 2s ease;
  }
  
  .reveal-item.active {
    opacity: 1;
    transform: translateY(0);
  }
  </style>
  