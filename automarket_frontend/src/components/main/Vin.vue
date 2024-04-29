<template>
    <div class="flex flex-col justify-center items-center bg-[#222] shadow-xl rounded-xl py-8 mb-14 reveal-item">
        <h1 class="uppercase text-3xl text-[#E6E6E6] font-bold mb-10 text-center">{{ $t('vin.search') }}</h1>
        <div class="w-full max-h-[400px] bg-[#222] rounded-xl">
          <!-- INPUT FIELD -->
          <form v-on:submit.prevent="submitVin" class="flex justify-around relative">
            <div class="w-[90%] h-[250px] flex md:flex-row flex-col items-center md:justify-around justify-center gap-2">
              <input 
                v-model="vinQuery" 
                id="vin" 
                type="text" 
                class="w-[90%] bg-[#E6E6E6] py-3 text-xl pl-4 rounded-lg" 
                :placeholder="$t('vin.placeholder')"
                @keydown.enter.prevent="searchOnEnter"
              >
              <button type="submit" class="uppercase bg-[#E6E6E6] text-black px-4 py-3.5 rounded-lg w-[90%] md:w-[25%] hover:bg-gray-100">search</button>
              <div v-if="errors.length > 0" class="absolute bottom-[5rem] md:text-lg text-center text-xs">
                  <div>
                      <p class="uppercase text-red-300" v-for="error in errors" v-bind:key="error">{{ error }}</p>
                  </div>
              </div>
            </div>
          </form>
        </div>
        <div class="p-6 rounded-lg flex justify-center items-center flex-col mt-4">
            <h2 class="text-2xl text-[#E6E6E6] font-semibold text-center">{{ $t('vin.understanding') }}</h2>
            <p class="mt-4 text-[#E6E6E6] w-[80%] text-center">{{ $t('vin.explanation') }}</p>
        </div>
      </div>
</template>

<script>
import { RouterLink } from 'vue-router'
import Trans from '@/i18n/translation'

export default {
  setup() {
    return {
      Trans,
      vinQuery: '',

    }
  },
  data() {
    return {
      errors: []
    }
  },
  mounted() {
    this.revealItemsOnScroll();
  },
  methods: {
    submitVin() {
      if (this.vinQuery.trim() === '') {
        this.errors = ["VIN cannot be empty"];
      } else if (/[IQO]/.test(this.vinQuery)) {
        this.errors = ["You can't use I, Q, and O in VIN decoder"];
      } else {
        this.$router.push(this.Trans.i18nRoute({ name: 'vin', query: { q: this.vinQuery }}));
      }
    },
    searchOnEnter(event) {
        if (!event.shiftKey) {
        event.preventDefault();
        this.submitVin();
        }
    },
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
  