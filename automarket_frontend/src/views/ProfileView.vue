<template>
    <div class="pt-14 h-screen">
        <div v-if="userStore.user.isAuthenticated">
            <div class="flex md:hidden mt-8 uppercase flex-col justify-center items-center">
                <h1 class="text-lg">{{ user.name }}</h1>
                <h1 class="uppercase mt-8">user settings</h1>
                <router-link :to="Trans.i18nRoute({ name: 'settings', props: {'id': userStore.user.id}})">
                    <button class="uppercase bg-black text-white px-3 py-2 rounded-md mt-2">settings</button>
                </router-link>
            </div>
            <div v-if="cars.length && !loading">
                <div class="flex items-center justify-center">
                    <h1 class="uppercase font-sans font-extralight lg:text-4xl md:text-4xl text-2xl mt-16">My Cars</h1>
                </div>
                <div class="flex justify-center items-center">
                    <div class="grid xl:grid-cols-3 lg:grid-cols-3 md:grid-cols-2 sm:grid-cols-2 gap-x-16 gap-y-20 mt-16">
                        <div v-for="car in cars" :key="car.id" class="w-[250px] h-[350px] shadow-2xl z-1 flex flex-col justify-start bg-[#E6E6E6] rounded-xl reveal-car">
                            <router-link :to="Trans.i18nRoute({ name: 'cardetail', params: {'id': car.id} })">
                                <img :v-if="car.main_image" :src="car.main_image.image_url" class="w-full h-44 rounded-t-xl transition-transform transform hover:scale-105 cursor-pointer" alt="">
                            </router-link>
                            <hr class="h-px bg-black border-0">
                            <span class="uppercase text-[10px] mt-2 ml-2 mb-2">{{ car.location }}</span>
                            <router-link :to="Trans.i18nRoute({ name: 'cardetail', params: {'id': car.id} })">
                                <span class="whitespace-nowrap overflow-hidden overflow-ellipsis cursor-pointer ml-2 uppercase text-lg text-gray-900 hover:text-red-900 font-semibold">{{ car.manufacturer }} - <span class="font-light text-black">{{ car.car_model }}</span></span>
                            </router-link>
                            <span class="uppercase font-light mt-4 ml-2 text-gray-900">{{ car.price }} <span class="font-semibold">$</span></span>
                            <hr class="h-px mt-4 bg-black border-0">
                            <div class="flex flex-row mt-2 ml-2">
                                <button @click="showDeleteModal(car.id)" class="uppercase bg-black text-white py-2 px-3 rounded-xl">delete</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="flex flex-col justify-center items-center mt-16" v-else-if="!cars.length && loading">
                <h1 class="uppercase font-sans font-extralight lg:text-4xl md:text-4xl text-2xl mt-16 text-center">Loading...</h1>
                <div class="grid xl:grid-cols-3 lg:grid-cols-3 md:grid-cols-2 sm:grid-cols-2 gap-x-16 gap-y-20 mt-16">
                    <div v-for="index in 8" :key="index" class="border w-[250px] border-gray-200 p-4">
                        <div class="animate-pulse space-y-2">
                            <div class="bg-[#222] rounded-lg h-48"></div>
                            <div class="flex-1 space-y-2">
                            <div class="h-16 bg-[#222] rounded-lg w-full"></div>
                                <div class="space-x-2 flex">
                                    <div class="h-8 bg-[#222] rounded-lg w-full"></div>
                                    <div class="h-8 bg-[#222] rounded-lg w-full"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div v-else class="h-screen">
                <h1 class="text-center uppercase text-4xl mt-60">no listing found</h1>
                <router-link :to="Trans.i18nRoute({ name: 'add'})">
                    <h1 class="text-center uppercase mt-20 underline text-2xl">CLICK HERE TO ADD LISTING CARS</h1>
                </router-link>
            </div>
        </div>
        <div v-else class="flex h-screen flex-col justify-center items-center">
            <img src="/warning.png" class="w-40 -mt-48" alt="warning">
            <h1 class="uppercase md:text-4xl text-xl mt-8">something went wrong!!!</h1>
        </div>
        <!-- MODAL -->
        <div v-if="showModal" class="font-sans antialiased fixed bottom-[25%] inset-x-0 px-4 pb-4 sm:inset-0 sm:flex sm:items-center sm:justify-center">
            <div class="fixed inset-0 transition-opacity">
                <div class="absolute inset-0 bg-black opacity-40"></div>
            </div>

            <div class="bg-white rounded-lg overflow-hidden shadow-xl transform transition-all sm:max-w-lg sm:w-full">
                <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
                <div class="sm:flex sm:items-start">
                    <div class="mx-auto flex-shrink-0 flex items-center justify-center h-12 w-12 rounded-full bg-red-100 sm:mx-0 sm:h-10 sm:w-10">
                    <svg class="h-6 w-6 text-red-600" stroke="currentColor" fill="none" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
                    </svg>
                    </div>
                    <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
                    <h3 class="text-lg leading-6 font-medium text-gray-900">
                        Delete car
                    </h3>
                    <div class="mt-2">
                        <p class="text-sm leading-5 text-gray-500">
                            Are you sure you want to delete your car? This car will be permanantly removed. This action cannot be undone.
                        </p>
                    </div>
                    </div>
                </div>
                </div>
                <div class="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
                    <span class="flex w-full rounded-md shadow-sm sm:ml-3 sm:w-auto">
                        <button @click="confirmDelete" type="button" class="inline-flex justify-center w-full rounded-md border border-transparent px-4 py-2 bg-black text-base leading-6 font-medium text-white shadow-sm hover:bg-red-500 focus:outline-none focus:border-red-700 focus:shadow-outline-red transition ease-in-out duration-150 sm:text-sm sm:leading-5">
                            Delete
                        </button>
                    </span>
                    <span class="mt-3 flex w-full rounded-md shadow-sm sm:mt-0 sm:w-auto">
                        <button @click="cancelDelete" type="button" class="inline-flex justify-center w-full rounded-md border border-gray-300 px-4 py-2 bg-white text-base leading-6 font-medium text-gray-700 shadow-sm hover:text-gray-500 focus:outline-none focus:border-blue-300 focus:shadow-outline transition ease-in-out duration-150 sm:text-sm sm:leading-5">
                            Cancel
                        </button>
                    </span>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Trans from '@/i18n/translation'
import axios from 'axios'
import { computed, watch, onMounted } from 'vue';
import { useUserStore } from '@/stores/user'
export default{
setup() {
    const userStore = useUserStore()
    const pageTitle = computed(() => `Profile of ${userStore.user.name}`);

    watch(pageTitle, (newTitle) => {
      document.title = newTitle;
    }, { immediate: true });
    return {
        pageTitle,
        Trans,
        userStore
    }
},
data() {
    return{
        cars: [],
        user: [],
        loading: false,
        showModal: false,
        carToDeleteId: null,
    }
},
methods: {
    getUserAndCars() {
      this.loading = true
      axios
        .get(`/api/profile/cars/${this.$route.params.id}/`)
        .then(response => {
            this.cars = response.data.cars
            this.user = response.data.user
        })
        .catch(error => {
            console.log(error)
        })
        .finally(() => {
            this.loading = false
        })
    },
    deleteCar(carId) {
      this.showModal = true
      this.carToDeleteId = carId
    },
    showDeleteModal(carId) {
      this.showModal = true
      this.carToDeleteId = carId
    },
    cancelDelete() {
      this.showModal = false
      this.carToDeleteId = null
    },
    confirmDelete() {
      if (this.carToDeleteId) {
        axios
          .delete(`/api/delete/${this.carToDeleteId}/`)
          .then(response => {
            if (response.data.message === 'deleted') {
              const index = this.cars.findIndex(car => car.id === this.carToDeleteId)
              if (index !== -1) {
                this.cars.splice(index, 1)
              }
            }
          })
          .catch(error => {
            console.log('Error deleting car: ', error)
          })
          .finally(() => {
            this.showModal = false
            this.carToDeleteId = null
          })
      }
    },
},
mounted() {
    this.getUserAndCars()
}
}
</script>