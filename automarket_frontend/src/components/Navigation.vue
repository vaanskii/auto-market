<template>
  <!-- Top Navigation -->
  <nav class="bg-white text-black fixed w-full py-2 z-10">
    <div class="container mx-auto px-4 md:flex items-center gap-6">
      <div class="flex justify-between w-full">
      <!-- logo-mobile-menu | navigation bar -->
        <div class="flex items-center justify-evenly md:w-auto md:h-6 h-10 w-full">
          <router-link :to="Trans.i18nRoute({ name: 'home' })" class="py-5 px-2 text-black font-bold uppercase">
            <img src="/car.png" alt="car" class="md:w-16 md:h-12 w-12 h-10">
          </router-link>
        <!-- Search input -->
        <div class="flex justify-center items-center mr-12 w-full">
          <form v-on:submit.prevent="submitSearch" class="md:mx-auto md:mt-[2px]">   
              <div class="relative">
                  <input 
                    type="search" 
                    id="default-search" 
                    class="w-full lg:w-[400px] p-4 outline-none h-10 ps-7 text-sm text-gray-900 border border-gray-300 hover:border-gray-400 rounded-lg hover:placeholder-gray-400" 
                    :placeholder="$t('nav.search')" 
                    required 
                    v-model="searchQuery"
                    @keydown.enter.prevent="searchOnEnter"
                    />
                  <button type="submit" class="absolute bottom-2 text-black right-3">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                      <path stroke-linecap="round" stroke-linejoin="round" d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z" />
                    </svg>
                  </button>
              </div>
          </form>

        </div>
        <!--Mobile menu-->
        <div class="md:hidden flex absolute right-5">
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
        <button @click="handleAddClick" type="button" class="bg-black md:flex hidden text-white items-center justify-evenly mr-8 rounded-lg w-[150px]">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
              <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v6m3-3H9m12 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
            </svg>
          <button class="py-2 px-3 block uppercase">{{ $t('nav.add') }}</button>
        </button>
        <Auth :isOpen="modalOpen" :onCloseModal="closeModal" v-if="!userStore.user.isAuthenticated"/>
        <!--Dropdown toggle-->
        <div class="relative md:block hidden">
          <button type="button" @click="toggleDropdown" class="dropdown-toggle mr-6 py-2 px-2 hover:bg-gray-100 hover:text-black flex items-center gap-2 rounded">
            <span class="pointer-events-none select-none uppercase w-[100px]">{{ $t('nav.language') }}</span>
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
          <div v-if="dropdownOpen" class="dropdown-menu flex flex-col md:absolute translate-transform ease-in-out duration-300 md:bg-black md:mt-6 md:-ml-28 text-sm md:text-white text-[#222] rounded-lg md:py-2 w-80">
            <LanguageSwitcher @click="dropdownOpen = false"/>
          </div>
        </transition>
        </div>
        <div v-if="!dropdownOpen" class="flex-col text-center md:hidden block sm:text-lg text-[15px]">
            <h1 class="uppercase mb-5">languages</h1>
            <LanguageSwitcher @click="menudropdownOpen = false"/>
            <hr class="h-[1.5px] my-8 bg-[#222] border-0">
            <button v-if="userStore.user.isAuthenticated" @click="handleLogout" class="uppercase bg-black text-white px-4 py-2 rounded-md">{{ $t('nav.logout') }}</button>
        </div>
        <div v-if="!userStore.user.isAuthenticated">
          <router-link :to="Trans.i18nRoute({ name: 'login' })" class="py-2 px-3 md:block hidden uppercase w-[85px] hover:bg-gray-100 hover:text-black">
            {{ $t('nav.login') }}
          </router-link>
        </div>
        <!-- Profile view dropdown -->
        <div 
            v-if="userStore.user.isAuthenticated" 
            @click="handleUserDropDown"
          >
          <div class="w-10 h-10 md:flex hidden cursor-pointer justify-center items-center border border-black rounded-full">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-6 h-6">
              <path fill-rule="evenodd" d="M7.5 6a4.5 4.5 0 1 1 9 0 4.5 4.5 0 0 1-9 0ZM3.751 20.105a8.25 8.25 0 0 1 16.498 0 .75.75 0 0 1-.437.695A18.683 18.683 0 0 1 12 22.5c-2.786 0-5.433-.608-7.812-1.7a.75.75 0 0 1-.437-.695Z" clip-rule="evenodd" />
            </svg>
          </div>
          <div class="relative">
            <div v-if="userDropdown" class="w-80 h-52 bg-[#E6E6E6] shadow-2xl absolute -right-0 rounded-md mt-4" @click.stop>
              <p class="text-center uppercase py-2 hover:border-black hover:border-b">{{ userStore.user.name }}</p>
              <p class="text-center uppercase py-2 hover:border-black hover:border-b">{{ userStore.user.email }}</p>
              <!-- Profile view -->
              <router-link @click="userDropdown = false" :to="Trans.i18nRoute({ name: 'profile', params: {'id': userStore.user.id} })" v-if="userStore.user.isAuthenticated && userStore.user.id" class="text-center">
                <p class="uppercase py-2 hover:border-black hover:border-b">{{ $t('nav.listing') }}</p>
              </router-link>
              <!-- Settings view -->
              <router-link @click="userDropdown = false" :to="Trans.i18nRoute({ name: 'settings', params: {'id': userStore.user.id} })" v-if="userStore.user.isAuthenticated" class="text-center">
                <p class="uppercase py-2 hover:border-black hover:border-b">{{ $t('nav.settings') }}</p>
              </router-link>
              <button 
                    @click="handleLogout" 
                    class="py-2 px-3 w-full absolute bottom-0 bg-[#222] rounded-t-lg text-white uppercase hover:bg-black"
                    >
                {{ $t('nav.logout') }}
              </button>
            </div>
          </div>
        </div>

      </div>
    </div>
  </nav>
      <!-- Bottom Navigation -->
  <nav class="bg-white text-black fixed bottom-0 w-full z-10">
    <div  class="flex justify-evenly md:hidden items-center w-full p-2">
      <router-link @click="menudropdownOpen = false" :to="Trans.i18nRoute({ name: 'home' })" class="flex flex-col items-center">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-9 h-9">
          <path stroke-linecap="round" stroke-linejoin="round" d="m2.25 12 8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
        </svg>
        <p class="uppercase text-[10px]">home</p>
      </router-link>
      <div class="relative">
        <button @click="handleAddClick" class="absolute -top-10 left-1 flex justify-center items-center transform -translate-x-1/2 w-14 h-14 rounded-full bg-[#222] text-white">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-14 h-14">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v6m3-3H9m12 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
          </svg>
        </button>
        <Auth :isOpen="modalOpen" :onCloseModal="closeModal" v-if="!userStore.user.isAuthenticated"/>
      </div>
      <div v-if="!userStore.user.isAuthenticated">
        <router-link @click="menudropdownOpen = false" :to="Trans.i18nRoute({ name: 'login' })" class="flex flex-col items-center">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-9 h-9">
            <path stroke-linecap="round" stroke-linejoin="round" d="M17.982 18.725A7.488 7.488 0 0 0 12 15.75a7.488 7.488 0 0 0-5.982 2.975m11.963 0a9 9 0 1 0-11.963 0m11.963 0A8.966 8.966 0 0 1 12 21a8.966 8.966 0 0 1-5.982-2.275M15 9.75a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
          </svg>
          <p class="text-[10px] uppercase">login</p>
        </router-link>
      </div>
      <div v-else>
        <router-link @click="menudropdownOpen = false" v-if="userStore.user.id" :to="Trans.i18nRoute({ name: 'profile', params: {'id': userStore.user.id} })" class="flex flex-col items-center">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-9 h-9">
            <path stroke-linecap="round" stroke-linejoin="round" d="M17.982 18.725A7.488 7.488 0 0 0 12 15.75a7.488 7.488 0 0 0-5.982 2.975m11.963 0a9 9 0 1 0-11.963 0m11.963 0A8.966 8.966 0 0 1 12 21a8.966 8.966 0 0 1-5.982-2.275M15 9.75a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
          </svg>
          <p class="text-[10px] uppercase">Profile</p>
        </router-link>
      </div>
    </div>
  </nav>
</template>

<script>
import Auth from './Auth.vue'
import { ChevronDownIcon, ChevronUpIcon, Bars3BottomRightIcon, XMarkIcon, DocumentMagnifyingGlassIcon } from '@heroicons/vue/24/solid'
import { RouterLink } from 'vue-router'
import LanguageSwitcher from './LanguageSwitcher.vue'
import Trans from '@/i18n/translation'
import { useUserStore } from '@/stores/user'
import { ref, onMounted } from 'vue';

export default {
  setup() {
    const userDropdown = ref(false);
    const handleUserDropDown = () => {
      userDropdown.value = !userDropdown.value;
    };
    const closeDropdown = (event) => {
      if (!event.target.closest('.w-10') && !event.target.closest('.w-52')) {
        userDropdown.value = false;
      }
    };
    onMounted(() => {
      window.addEventListener('click', closeDropdown);
    });
    const userStore = useUserStore()
    return {
      Trans,
      searchQuery: '',
      userStore,
      userDropdown,
      handleUserDropDown
    }
  },
  data() {
    return {
      dropdownOpen: false,
      menudropdownOpen: false,
      modalOpen: false,
    };
  },
  components:{
    ChevronDownIcon,
    ChevronUpIcon,
    BurgerIcon: Bars3BottomRightIcon,
    xIcon: XMarkIcon,
    searchIcon: DocumentMagnifyingGlassIcon,
    Auth,
    LanguageSwitcher
  },
  methods: {
    handleUserDropDown() {
      this.userDropdown = !this.userDropdown
    },
    logout() {
      this.userStore.removeToken()
      this.$router.push(this.Trans.i18nRoute({ name: 'login' }));
    },
    handleLogout() {
        this.logout();
        this.menudropdownOpen = false;
    },
    submitSearch() {
      if (this.searchQuery.trim() !== '') {
        this.$router.push(this.Trans.i18nRoute({ name: 'search', query: { q: this.searchQuery }}));
      }
    },
    searchOnEnter(event) {
        if (!event.shiftKey) {
        event.preventDefault();
        this.submitSearch();
        this.isBurgerVisible = false;
        }
    },
    openModal() {
      this.modalOpen = true
    },
    closeModal() {
      this.modalOpen = false
    },
    handleAddClick() {
      if(!this.userStore.user.isAuthenticated) {
        this.openModal()
      }else {
        this.$router.push(this.Trans.i18nRoute({ name: 'add' }));
      }
    },
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
  },
  mounted() {
    if (localStorage.getItem('showCustomCursor') !== null) {
      this.showCustomCursor = localStorage.getItem('showCustomCursor') === 'true'
    }
    window.addEventListener('click', this.closeDropdowns)
  },
  beforeDestroy() {
    window.removeEventListener('click', this.closeDropdowns)
  }
}
</script>

<style scoped>
input[type="search"]::-webkit-search-cancel-button {
    -webkit-appearance: none;
}
</style>
