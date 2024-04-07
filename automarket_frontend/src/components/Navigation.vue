<template>
  <nav class="bg-white text-black fixed w-full py-2 z-10">
    <div class="container mx-auto px-4 md:flex items-center gap-6">
      <div class="flex justify-between w-full">
      <!-- logo-mobile-menu | navigation bar -->
        <div class="flex items-center justify-evenly md:w-auto md:h-6 w-full">
          <a href="/" class="py-5 px-2 text-black hidden  lg:block font-bold uppercase">
            <img src="/car.png" alt="car" class="w-12 h-12">
          </a>
        <!-- Search input -->
        <div>
          <form class="md:mx-auto md:mt-[2px] md:ml-14 w-72">   
              <div class="relative">
                  <input type="search" id="default-search" class="w-full p-4 outline-none h-10 ps-7 text-sm text-gray-900 border border-gray-300 hover:border-gray-400 rounded-lg hover:placeholder-gray-400" placeholder="Search" required />
                  <button type="submit" class="absolute bottom-2 text-black right-3">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                      <path stroke-linecap="round" stroke-linejoin="round" d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z" />
                    </svg>
                  </button>
              </div>
          </form>
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
      <div :class="{ 'hidden': !menudropdownOpen}" class="bg-white md:h-auto h-screen md:flex md:flex-row flex-col items-center justify-start md:space-x-1 md:mt-0 md:ml-0 ml-3 mt-10 md:pb-0 navigation-menu">
        <button type="button" class="bg-black md:flex hidden text-white items-center justify-center mr-6 rounded-lg w-28">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
              <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v6m3-3H9m12 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
            </svg>
          <a href="#" class="py-2 px-3 block uppercase">add</a>
        </button>
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
          <div v-if="dropdownOpen" class="dropdown-menu flex flex-col md:absolute translate-transform ease-in-out duration-300 md:bg-[#444] md:mt-6 md:-ml-20 text-sm md:text-white text-[#222] rounded-lg md:py-2 w-80">
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
          </div>
        </transition>
        </div>
        <a href="#" class="py-2 px-3 block uppercase">Login</a>
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
