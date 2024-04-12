<template>
  <!-- Top Navigation -->
  <nav class="bg-white text-black fixed w-full py-2 z-10">
    <div class="container mx-auto px-4 md:flex items-center gap-6">
      <div class="flex justify-between w-full">
      <!-- logo-mobile-menu | navigation bar -->
        <div class="flex items-center justify-evenly md:w-auto md:h-6 w-full">
          <a href="/" class="py-5 px-2 text-black hidden  md:block font-bold uppercase">
            <img src="/car.png" alt="car" class="w-12 h-12">
          </a>
        <!-- Search input -->
        <div class="flex justify-center items-center lg:w-[500px] w-[350px]">
          <form class="md:mx-auto md:mt-[2px] md:ml-14 w-[90%]">   
              <div class="relative">
                  <input type="search" id="default-search" class="w-full p-4 outline-none h-10 ps-7 text-sm text-gray-900 border border-gray-300 hover:border-gray-400 rounded-lg hover:placeholder-gray-400" placeholder="Search" required />
                  <button type="submit" class="absolute bottom-2 text-black right-3">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                      <path stroke-linecap="round" stroke-linejoin="round" d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z" />
                    </svg>
                  </button>
              </div>
          </form>
          <!-- Mouse checkbox -->
          <div class="flex-col justify-center ml-5 md:mt-0 mt-2 lg:block hidden">
            <label for="foobar3" class="flex flex-col flex-wrap items-center uppercase text-[10px] cursor-pointer mb-4 md:mb-0">
              mouse
                <div class="relative">
                  <input id="foobar3" type="checkbox" v-model="showCustomCursor" class="hidden">
                  <div class="toggle__line w-12 h-6 bg-gray-200 rounded-full shadow-inner"></div>
                  <div class="toggle__dot absolute w-5 h-5 bg-white rounded-full shadow inset-y-0 left-0"></div>
                </div>
            </label>
            <Mouse v-if="showCustomCursor"/>
          </div>

        </div>
        <!--Mobile menu-->
        <div class="md:hidden flex items-center">
            <button type="button" @click="toggleMenuDropdown" class="mobile-menu-button">
              <div class="flex items-center">
                <BurgerIcon 
                  class="w-6 h-6 transition-transform ease-in duration-300 absolute"
                  :class="{'rotate-180 opacity-0': menudropdownOpen, 'rotate-0 opacity-100': !menudropdownOpen}"
                />
                <xIcon 
                  class="w-6 h-6 transition-transform ease-in duration-300"
                  :class="{'rotate-180 opacity-0': !menudropdownOpen, 'rotate-0 opacity-100': menudropdownOpen}"
                />
            </div>
          </button>
        </div>          
      </div>
      </div>
      <!-- Pages -->
      <div :class="{ 'hidden': !menudropdownOpen}" class="bg-white md:h-auto h-screen md:flex md:flex-row flex-col items-center justify-start md:space-x-1 md:mt-0 md:ml-0 ml-3 mt-10 md:pb-0 navigation-menu" :style="{ 'z-index': menudropdownOpen ? '10000' : 'auto' }">
        <button type="button" class="bg-black md:flex hidden text-white items-center justify-center mr-6 rounded-lg w-28">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
              <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v6m3-3H9m12 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
            </svg>
          <a href="#" class="py-2 px-3 block uppercase">add</a>
        </button>
        <!--Dropdown toggle-->
        <div class="relative md:block hidden">
          <button type="button" @click="toggleDropdown" class="dropdown-toggle py-2 px-3 hover:bg-gray-100 hover:text-black flex items-center gap-2 rounded">
            <span class="pointer-events-none select-none uppercase">Services</span>
            <div class="pointer-events-none select-none flex items-center">
              <ChevronDownIcon
                class="w-4 h-4 pointer-events-none transition-transform ease-in duration-300 absolute"
                :class="{ 'rotate-180 opacity-0': dropdownOpen, 'rotate-0 opacity-100': !dropdownOpen }"
              />
              <ChevronUpIcon
                class="w-4 h-4 pointer-events-none transition-transform ease-in duration-300"
                :class="{ 'rotate-180 opacity-0': !dropdownOpen, 'rotate-0 opacity-100': dropdownOpen }"
              />
            </div>
          </button>
          <!-- Dropdown menu -->
          <transition
              enter-active-class="transform transition duration-500 ease-custom"
              enter-class="-translate-y-1/2 scale-y-0 opacity-0"
              enter-to-class="translate-y-0 scale-y-100 opacity-100"
              leave-active-class="transform transition duration-300 ease-custom"
              leave-class="translate-y-0 scale-y-100 opacity-100"
              leave-to-class="-translate-y-1/2 scale-y-0 opacity-0"
          >
          <div v-if="dropdownOpen" class="dropdown-menu flex flex-col md:absolute translate-transform ease-in-out duration-300 md:bg-[#222] md:mt-6 md:-ml-28 text-sm md:text-white text-[#222] rounded-lg md:py-2 w-80">
            <a href="#" class="block px-6 py-2 rounded md:hover:bg-black uppercase">Car Maintenance Services</a>
            <a href="#" class="block px-6 py-2 rounded md:hover:bg-black uppercase">Car Wash and Detailing</a>
            <a href="#" class="block px-6 py-2 rounded md:hover:bg-black uppercase">Roadside Assistance</a>
            <a href="#" class="block px-6 py-2 rounded md:hover:bg-black uppercase">Extended Warranty Plans</a>
            <a href="#" class="block px-6 py-2 rounded md:hover:bg-black uppercase">Insurance Services</a>
            <a href="#" class="block px-6 py-2 rounded md:hover:bg-black uppercase">Vehicle Customization</a>
            <a href="#" class="block px-6 py-2 rounded md:hover:bg-black uppercase">Transportation Services</a>
            <a href="#" class="block px-6 py-2 rounded md:hover:bg-black uppercase">Lease-to-Own Options</a>
            <a href="#" class="block px-6 py-2 rounded md:hover:bg-black uppercase">Concierge Services</a>
            <a href="#" class="block px-6 py-2 rounded md:hover:bg-black uppercase">Car Rental Subscription Services</a>
          </div>
        </transition>
        </div>
        <div v-if="!dropdownOpen" class="flex-col text-center md:hidden block sm:text-lg text-[15px]">
            <a href="#" class="block px-6 py-2 rounded md:hover:bg-gray-300 uppercase">Car Maintenance Services</a>
            <a href="#" class="block px-6 py-2 rounded md:hover:bg-gray-300 uppercase">Car Wash and Detailing</a>
            <a href="#" class="block px-6 py-2 rounded md:hover:bg-gray-300 uppercase">Roadside Assistance</a>
            <a href="#" class="block px-6 py-2 rounded md:hover:bg-gray-300 uppercase">Extended Warranty Plans</a>
            <a href="#" class="block px-6 py-2 rounded md:hover:bg-gray-300 uppercase">Insurance Services</a>
            <a href="#" class="block px-6 py-2 rounded md:hover:bg-gray-300 uppercase">Vehicle Customization</a>
            <a href="#" class="block px-6 py-2 rounded md:hover:bg-gray-300 uppercase">Transportation Services</a>
            <a href="#" class="block px-6 py-2 rounded md:hover:bg-gray-300 uppercase">Lease-to-Own Options</a>
            <a href="#" class="block px-6 py-2 rounded md:hover:bg-gray-300 uppercase">Concierge Services</a>
            <a href="#" class="block px-6 py-2 rounded md:hover:bg-gray-300 uppercase">Car Rental Subscription Services</a>
            <hr class="h-[1.5px] my-8 bg-[#222] border-0">
          </div>
        <a href="#" class="py-2 px-3 md:block hidden uppercase">Login</a>
      </div>
    </div>
  </nav>
      <!-- Bottom Navigation -->
  <nav class="bg-white text-black fixed bottom-0 w-full z-10">
    <div :class="{'justify-evenly': !userIsActivated, 'justify-around ml-2': userIsActivated}" class="flex md:hidden items-center w-full p-2">
      <a href="/" class="flex flex-col items-center">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-7 h-7">
          <path stroke-linecap="round" stroke-linejoin="round" d="m2.25 12 8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
        </svg>
        <p class="uppercase text-[10px]">home</p>
      </a>
      <a href="#" v-if="userIsActivated" class="flex flex-col items-center">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-7 h-7">
          <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
        </svg>
        <p class="uppercase text-[10px]">saved</p>
      </a>
      <div class="relative">
        <a href="#" class="absolute -top-10 left-1/2 flex justify-center items-center transform -translate-x-1/2 w-12 h-12 rounded-full bg-[#222] text-white">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-12 h-12">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v6m3-3H9m12 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
          </svg>
        </a>
      </div>
      <a href="#" v-if="userIsActivated" class="flex flex-col items-center">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-7 h-7">
          <path stroke-linecap="round" stroke-linejoin="round" d="M6 13.5V3.75m0 9.75a1.5 1.5 0 0 1 0 3m0-3a1.5 1.5 0 0 0 0 3m0 3.75V16.5m12-3V3.75m0 9.75a1.5 1.5 0 0 1 0 3m0-3a1.5 1.5 0 0 0 0 3m0 3.75V16.5m-6-9V3.75m0 3.75a1.5 1.5 0 0 1 0 3m0-3a1.5 1.5 0 0 0 0 3m0 9.75V10.5" />
        </svg>
        <p class="uppercase text-[10px]">settings</p>
      </a>
      <a href="#" class="flex flex-col items-center">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-7 h-7">
          <path stroke-linecap="round" stroke-linejoin="round" d="M17.982 18.725A7.488 7.488 0 0 0 12 15.75a7.488 7.488 0 0 0-5.982 2.975m11.963 0a9 9 0 1 0-11.963 0m11.963 0A8.966 8.966 0 0 1 12 21a8.966 8.966 0 0 1-5.982-2.275M15 9.75a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
        </svg>
        <p class="text-[10px] uppercase">login</p>
      </a>
    </div>
  </nav>
</template>

<script>
// importing heroicons
import { ChevronDownIcon, ChevronUpIcon, Bars3BottomRightIcon, XMarkIcon, DocumentMagnifyingGlassIcon } from '@heroicons/vue/24/solid'
import { RouterLink } from 'vue-router'
import Mouse from './Mouse.vue'

export default {
  data() {
    return {
      dropdownOpen: false,
      menudropdownOpen: false,
      userIsActivated: true,
      showCustomCursor: true
    };
  },
  watch: {
    showCustomCursor(value) {
      localStorage.setItem('showCustomCursor', value)
      document.documentElement.style.cursor = value ? 'none' : 'auto'
    }
  },
  components:{
    ChevronDownIcon,
    ChevronUpIcon,
    BurgerIcon: Bars3BottomRightIcon,
    xIcon: XMarkIcon,
    searchIcon: DocumentMagnifyingGlassIcon,
    Mouse
  },
  methods: {
    toggleMenuDropdown() {
      this.menudropdownOpen = !this.menudropdownOpen
    },
    toggleDropdown() {
      this.dropdownOpen = !this.dropdownOpen;
      if (this.dropdownOpen) {
        // Close other open dropdown menus
        document.querySelectorAll('.dropdown-menu').forEach(menu => {
          menu.classList.add('hidden')
        });
      }
    },
    closeDropdowns(event) {
      if (!event.target.matches('.dropdown-toggle')) {
        document.querySelectorAll('.dropdown-menu').forEach(menu => {
          if (!menu.contains(event.target)) {
            menu.classList.add('hidden')
            this.dropdownOpen = false
          }
        })
      }
    },
    handleResize() {
      const screenWidth = window.innerWidth
      if (screenWidth < 1024) {
        this.showCustomCursor = false
      } else {
        this.showCustomCursor = localStorage.getItem('showCustomCursor') === 'true'
      }
    }
  },
  mounted() {
    if (localStorage.getItem('showCustomCursor') !== null) {
      this.showCustomCursor = localStorage.getItem('showCustomCursor') === 'true'
    }
    window.addEventListener('click', this.closeDropdowns)
    window.addEventListener('resize', this.handleResize)
    this.handleResize()
  },
  beforeDestroy() {
    window.removeEventListener('click', this.closeDropdowns)
    window.removeEventListener('resize', this.handleResize)
  }
}
</script>

<style scoped>
input[type="search"]::-webkit-search-cancel-button {
    -webkit-appearance: none;
}
.toggle__dot {
  top: 2px;
  left: 3.5px;
  transition: all 0.3s ease-in-out;
}

input:checked ~ .toggle__dot {
  transform: translateX(100%);
  left: 5px;
  background-color:black;
}
</style>
