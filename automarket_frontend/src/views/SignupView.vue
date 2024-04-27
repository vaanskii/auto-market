<template>
    <div class="md:pt-0 pt-14">
        <div class="flex items-center min-h-screen p-4 lg:justify-center md:mt-0 mt-20">
      <div
        class="flex flex-col overflow-hidden bg-white rounded-md shadow-4xl max md:flex-row md:flex-1 lg:max-w-screen-md"
      >
        <div
          class="p-4 py-6 text-white bg-[#222] md:w-80 md:flex-shrink-0 md:flex md:flex-col md:items-center md:justify-evenly"
        >
          <div class="my-3 text-4xl font-bold tracking-wider text-center">
            <p class="uppercase">autohub</p>
          </div>
          <p class="mt-6 font-normal text-center text-gray-300 md:mt-0">
            {{ $t('login.paragraph') }}
          </p>
          <p class="flex flex-col items-center justify-center mt-10 text-center">
            <span>{{ $t('signup.account') }}</span>
            <router-link :to="Trans.i18nRoute({ name: 'login' })" class="underline mt-px">Log in!</router-link>
          </p>
          <p class="mt-6 text-sm text-center text-gray-300">
            Read our <a href="#" class="underline">terms</a> and <a href="#" class="underline">conditions</a>
          </p>
        </div>
        <div class="p-5 bg-[#E6E6E6] md:flex-1">
          <h3 class="my-4 text-2xl font-semibold text-gray-700 uppercase">{{ $t('signup.createacc') }}</h3>
          <form v-on:submit.prevent="submitForm" action="#" class="flex relative flex-col space-y-5">
            <div class="flex flex-col space-y-1 mb-4">
              <label for="email" class="text-sm font-semibold text-gray-500">{{ $t('changeinfo.email') }}</label>
              <input
                type="email"
                id="email"
                autofocus
                v-model="form.email"
                placeholder="Enter your mail"
                class="px-4 py-2 transition duration-300 border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black"
                autocomplete="email"
              />
              <p v-if="errors.includes('User with this Email already exists.')" class="text-white px-2 rounded-xl bg-red-500 absolute top-[68px] text-sm mt-1">
                Email already exists.
              </p>
              <p v-if="errors.includes('Your email is missing')" class="text-white px-2 rounded-xl bg-red-500 absolute top-[68px] text-sm mt-1">
                Your email is missing.
              </p>
            </div>
            <div class="flex flex-col space-y-1">
              <label for="name" class="text-sm font-semibold text-gray-500">{{ $t('changeinfo.name') }}</label>
              <input
                type="text"
                id="name"
                autofocus
                v-model="form.name"
                placeholder="Enter your name"
                class="px-4 py-2 transition duration-300 border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black"
                autocomplete="email"
              />
              <p v-if="errors.includes('Your name is missing')" class="text-white px-2 rounded-xl bg-red-500 absolute top-[172px] text-sm">
                Your name is missing.
              </p>
            </div>
            <!-- Mobile number and country code -->
            <div class="group w-full">
              <label for="tel" class="text-sm font-semibold flex mt-6 text-gray-500">{{ $t('changeinfo.mobile_number') }}</label>
              <div class="relative flex items-center">
                <input
                    type="tel"
                    id="tel"
                    autofocus
                    v-model="form.mobile_number"
                    placeholder="Mobile number"
                    class="peer mt-2 relative h-10 w-full rounded-md bg-gray-50 pl-32 pr-4 outline-none"
                    autocomplete="tel"
                    @input="restrictNumericInput"
                />
                <p v-if="errors.includes('User with this Mobile number already exists.')" class="text-white px-2 rounded-xl bg-red-500 absolute top-12 text-sm mt-1">
                Mobile number already exists.
              </p>
              <p v-if="errors.includes('Your mobile number is missing')" class="text-white px-2 rounded-xl bg-red-500 absolute top-12 text-sm mt-1">
                Your mobile number is missing.
              </p>
                <select v-model="form.country_code" id="country_code" class="text-center mt-2 absolute h-10 w-28 outline-none rounded-l-md text-sm bg-[#222] font-semibold text-white ">
                    <option value="+995">Geo (+995)</option>
                    <option value="+1">USA (+1)</option>
                </select>
              </div>
            </div>

            <div class="flex flex-col relative space-y-1">
              <div class="flex items-center justify-between">
                <label for="password" class="text-sm mt-6 font-semibold text-gray-500">{{ $t('signup.password1') }}</label>
              </div>
              <input
                type="password"
                id="password"
                placeholder="*********"
                v-model="form.password1"
                class="px-4 py-2 transition duration-300 border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black"
                autocomplete="current-password"
              />
              <p v-if="errors.includes('Password is missing')" class="text-white px-2 rounded-xl bg-red-500 absolute top-[90px] text-sm mt-1">
                Password is missing
              </p>
            </div>
            <div class="flex relative flex-col space-y-1">
              <div class="flex items-center justify-between">
                <label for="password2" class="text-sm mt-4 font-semibold text-gray-500">{{ $t('signup.password2') }}</label>
              </div>
              <input
                type="password"
                id="password2"
                v-model="form.password2"
                placeholder="*********"
                class="px-4 py-2 transition duration-300 border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black"
                autocomplete="current-password"
              />
              <p v-if="errors.includes('Passwords not matching!')" class="text-white px-2 rounded-xl bg-red-500 absolute top-[86px] text-sm mt-1">
                Passwords not matching!
              </p>
            </div>
            <div>
                <button 
                    class="btn2 w-full mt-10 px-10 py-5 text-lg relative transition-colors border border-black rounded-md uppercase font-semibold tracking-wider leading-none overflow-hidden hover:text-white" 
                    type="submit"
                    >
                    <span class="absolute inset-0 bg-[#222]"></span>
                    <span class="absolute inset-0 flex justify-center items-center font-bold">{{ $t('signup.sign-up') }}</span>
                </button>
                <transition name="fade" mode="out-in">
                <div v-if="submitSuccessfully" key="confirmation" id="toast-simple" class="flex mt-4  items-center w-full p-4 space-x-4 rtl:space-x-reverse text-black uppercase bg-green-300 rounded-lg shadow-2xl" role="alert">
                    <svg class="w-8 h-8 text-black rotate-45" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 20">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m9 17 8 2L9 1 1 19l8-2Zm0 0V9"/>
                    </svg>
                    <p class="ps-4 text-sm font-normal">We've sent a confirmation message to your email. Please check your inbox.</p>
                </div>
              </transition>
            </div>
          </form>
        </div>
      </div>
    </div>
    </div>
</template>

<script>
import { RouterLink } from 'vue-router'
import Trans from '@/i18n/translation'
import axios from 'axios'
import { useUserStore } from '@/stores/user'
export default {
  setup() {
    const userStore = useUserStore()
    return {
      Trans,
      userStore
    }
  },
  data() {
    return {
      form: {
        email: '',
        name: '',
        mobile_number: '',
        password1: '',
        password2: '',
        country_code: '+995'
      },
      errors: [],
      submitSuccessfully: false
    }
  },
  methods: {
    submitForm() {
      this.errors = []

      this.form.country_code = this.form.country_code; 

      if (this.form.email === '') {
        this.errors.push('Your email is missing')
      }
      if (this.form.name === '') {
        this.errors.push('Your name is missing')
      }
      if (this.form.mobile_number === '') {
        this.errors.push('Your mobile number is missing')
      }
      if (this.form.password1 === '') {
        this.errors.push('Password is missing')
      }
      if (this.form.password1 !== this.form.password2) {
        this.errors.push('Passwords not matching!')
      }

      if (this.errors.length === 0) {
        axios
        .post('/api/signup/', this.form)
        .then(response => {
          if (response.data.message === 'success') {
            
            this.form.email = ''
            this.form.name = ''
            this.form.mobile_number = ''
            this.form.password1 = ''
            this.form.password2 = ''
            this.form.mobile_number = ''
            this.submitSuccessfully = true
            setTimeout(() => {
              this.submitSuccessfully = false;
            }, 5000);
          }else{
            const errorMessage = JSON.parse(response.data.message);
            for (const key in errorMessage) {
              errorMessage[key].forEach(error => {
                this.errors.push(error.message);
              }); 
            }
          }
        })
        .catch(error => {
          console.log(error)
        })
      }
    },
    restrictNumericInput(event) {
      this.form.mobile_number = this.form.mobile_number.replace(/\D/g, '');
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
.btn2 span:first-child{
  transform: translateX(-101%);
  transition: transform .3s ease-in
}
.btn2:hover span{
  transform: translateX(0)
}
.fade-enter-active,
  .fade-leave-active {
    transition: opacity 0.5s;
  }
  .fade-enter-from,
  .fade-leave-to {
    opacity: 0;
  }
</style>