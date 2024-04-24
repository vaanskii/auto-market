<template>
    <div class="pt-14">
        <div v-if="userStore.user.isAuthenticated">
            <div class="flex md:hidden mt-8 uppercase flex-col justify-center items-center">
                <h1 class="text-lg">{{ user.name }}</h1>
                <h1 class="uppercase mt-8">user settings</h1>
                <router-link :to="Trans.i18nRoute({ name: 'settings', props: {'id': userStore.user.id}})">
                    <button class="uppercase bg-black text-white px-3 py-2 rounded-md mt-2">settings</button>
                </router-link>
            </div>
            <div v-if="cars.length">
                <div class="flex items-center justify-center">
                    <h1 class="uppercase font-sans font-extralight lg:text-4xl md:text-4xl text-2xl mt-16">My Cars</h1>
                </div>
                <div class="flex justify-center items-center">
                    <div class="grid xl:grid-cols-3 lg:grid-cols-3 md:grid-cols-2 sm:grid-cols-2 gap-x-16 gap-y-20 mt-16">
                        <div v-for="car in cars" :key="car.id" class="max-w-[280px] h-[350px] shadow-2xl z-1 w-full flex flex-col justify-start bg-[#E6E6E6] rounded-xl reveal-car">
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
                                <button class="uppercase bg-black text-white py-2 px-3 rounded-xl">delete</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div v-else class="flex flex-col justify-center items-center">
            <img src="/warning.png" class="w-64 mt-20" alt="warning">
            <h1 class="uppercase md:text-4xl text-xl mt-8">something went wrong!!!</h1>
        </div>
    </div>
</template>

<script>
import Trans from '@/i18n/translation'
import axios from 'axios'
import { useUserStore } from '@/stores/user'
export default{
setup() {
    const userStore = useUserStore()
    return {
        Trans,
        userStore
    }
},
data() {
    return{
        cars: [],
        user: []
    }
},
methods: {
    getUserAndCars() {
      axios
        .get(`/api/profile/cars/${this.$route.params.id}/`)
        .then(response => {
            this.cars = response.data.cars
            this.user = response.data.user
        })
        .catch(error => {
            console.log(error)
        })
    }
},
mounted() {
    this.getUserAndCars()
}
}
</script>