<template>
    <nav class="bg-white text-black fixed w-full py-2">
      <div class="container mx-auto px-4 md:flex items-center gap-6 ">
        <!-- logo-mobile-menu | navigation bar -->
        <div class="flex items-center justify-between md:w-auto md:h-6 w-full">
          <a href="/" class="py-5 px-2 text-black flex-1 font-bold uppercase">
            <img src="/car.png" alt="car" class="w-12 h-12 hidden md:block">
          </a>
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
        <!-- Search input -->
        <div>
          <form class="max-w-md md:mx-auto md:mt-[2px] -mt-[40px] w-72">   
              <div class="relative">
                  <input type="search" id="default-search" class="w-full p-4 outline-none h-10 ps-7 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50  dark:placeholder-black" placeholder="Search" required />
                  <button type="submit" class="absolute bottom-2 text-black right-3">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                      <path stroke-linecap="round" stroke-linejoin="round" d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z" />
                    </svg>
                  </button>
              </div>
          </form>
        </div>
        <!-- Pages -->
        <div :class="{ 'hidden': !menudropdownOpen,}" class="bg-white md:h-auto h-screen md:flex md:flex-row flex-col items-center justify-start md:space-x-1 pb-3 md:pb-0 navigation-menu">
          <a href="#" class="py-2 px-3 block uppercase">Home</a>
          <a href="#" class="py-2 px-3 block uppercase">About</a>
          <!--Dropdown toggle-->
          <div class="relative">
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
            <div v-if="dropdownOpen" class="dropdown-menu flex flex-col md:absolute translate-transform ease-in-out duration-300 md:bg-white md:mt-6 text-black rounded-lg md:py-2 w-56">
              <a href="#" class="block px-6 py-2 rounded md:hover:bg-gray-300 uppercase">Web Design</a>
              <a href="#" class="block px-6 py-2 rounded md:hover:bg-gray-300 uppercase">Web Development</a>
              <a href="#" class="block px-6 py-2 rounded md:hover:bg-gray-300 uppercase">SEO</a>
            </div>
          </transition>
          </div>
          <a href="#" class="py-2 px-3 block uppercase">Contact</a>
        </div>
      </div>
    </nav>
</template>

<script>
// importing heroicons
import { ChevronDownIcon, ChevronUpIcon, Bars3BottomRightIcon, XMarkIcon, DocumentMagnifyingGlassIcon } from '@heroicons/vue/24/solid'
export default {
  data() {
    return {
      dropdownOpen: false,
      menudropdownOpen: false,
    };
  },
  components:{
    ChevronDownIcon,
    ChevronUpIcon,
    BurgerIcon: Bars3BottomRightIcon,
    xIcon: XMarkIcon,
    searchIcon: DocumentMagnifyingGlassIcon
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
          menu.classList.add('hidden');
        });
      }
    },
    closeDropdowns(event) {
      if (!event.target.matches('.dropdown-toggle')) {
        document.querySelectorAll('.dropdown-menu').forEach(menu => {
          if (!menu.contains(event.target)) {
            menu.classList.add('hidden');
            this.dropdownOpen = false
          }
        });
      }
    }
  },
  mounted() {
    window.addEventListener('click', this.closeDropdowns);
  },
  beforeDestroy() {
    window.removeEventListener('click', this.closeDropdowns);
  }
};
</script>

<style>
.ease-custom {
  transition-timing-function: cubic-bezier(.61,-0.53,.43,1.43);
}
input[type="search"]::-webkit-search-cancel-button {
    -webkit-appearance: none;
}
</style>
