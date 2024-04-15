<template>
    <div class="md:pt-0 pt-14">
        <div class="flex items-center min-h-screen p-4 bg-gray-100 lg:justify-center md:mt-0 mt-20">
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
        <div class="p-5 bg-white md:flex-1">
          <h3 class="my-4 text-2xl font-semibold text-gray-700 uppercase">Create account</h3>
          <form action="#" class="flex flex-col space-y-5">
            <div class="flex flex-col space-y-1">
              <label for="email" class="text-sm font-semibold text-gray-500">Email address</label>
              <input
                type="email"
                id="email"
                autofocus
                placeholder="Enter your mail"
                class="px-4 py-2 transition duration-300 border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black"
                autocomplete="email"
              />
            </div>
            <div class="flex flex-col space-y-1">
              <label for="tel" class="text-sm font-semibold text-gray-500">Mobile number</label>
              <input
                type="tel"
                id="tel"
                autofocus
                placeholder="Mobile number"
                class="px-4 py-2 transition duration-300 border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black"
                autocomplete="tel"
              />
            </div>
            <div class="flex flex-col space-y-1">
              <div class="flex items-center justify-between">
                <label for="password" class="text-sm font-semibold text-gray-500">Password</label>
              </div>
              <input
                type="password"
                id="password"
                placeholder="*********"
                class="px-4 py-2 transition duration-300 border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black"
                autocomplete="current-password"
              />
            </div>
            <div class="flex flex-col space-y-1">
              <div class="flex items-center justify-between">
                <label for="password2" class="text-sm font-semibold text-gray-500">Repeat password</label>
              </div>
              <input
                type="password"
                id="password2"
                placeholder="*********"
                class="px-4 py-2 transition duration-300 border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black"
                autocomplete="current-password"
              />
            </div>
            <div>
                <button 
                    class="btn2 w-full px-10 py-5 text-lg relative transition-colors border border-black rounded-md uppercase font-semibold tracking-wider leading-none overflow-hidden hover:text-white" 
                    type="submit"
                    >
                    <span class="absolute inset-0 bg-[#222]"></span>
                    <span class="absolute inset-0 flex justify-center items-center font-bold">{{ $t('signup.sign-up') }}</span>
                </button>
            </div>
            <div class="flex flex-col space-y-5">
              <span class="flex items-center justify-center space-x-2">
                <span class="h-px bg-gray-400 w-14"></span>
                <span class="font-normal text-gray-500">or connect with</span>
                <span class="h-px bg-gray-400 w-14"></span>
              </span>
              <div class="flex flex-col space-y-4">
                <a
                  href="#"
                  class="flex items-center justify-center px-4 py-2 space-x-2 transition-colors duration-300 border border-gray-800 rounded-md group hover:bg-black focus:outline-none"
                >
                  <span>
                    <svg class="w-6 h-6" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="100" height="100" viewBox="0 0 48 48">
                        <path fill="#fbc02d" d="M43.611,20.083H42V20H24v8h11.303c-1.649,4.657-6.08,8-11.303,8c-6.627,0-12-5.373-12-12	s5.373-12,12-12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C12.955,4,4,12.955,4,24s8.955,20,20,20	s20-8.955,20-20C44,22.659,43.862,21.35,43.611,20.083z"></path><path fill="#e53935" d="M6.306,14.691l6.571,4.819C14.655,15.108,18.961,12,24,12c3.059,0,5.842,1.154,7.961,3.039	l5.657-5.657C34.046,6.053,29.268,4,24,4C16.318,4,9.656,8.337,6.306,14.691z"></path><path fill="#4caf50" d="M24,44c5.166,0,9.86-1.977,13.409-5.192l-6.19-5.238C29.211,35.091,26.715,36,24,36	c-5.202,0-9.619-3.317-11.283-7.946l-6.522,5.025C9.505,39.556,16.227,44,24,44z"></path><path fill="#1565c0" d="M43.611,20.083L43.595,20L42,20H24v8h11.303c-0.792,2.237-2.231,4.166-4.087,5.571	c0.001-0.001,0.002-0.001,0.003-0.002l6.19,5.238C36.971,39.205,44,34,44,24C44,22.659,43.862,21.35,43.611,20.083z"></path>
                    </svg>
                  </span>
                  <span class="text-sm font-medium text-black group-hover:text-white">Google</span>
                </a>
              </div>
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
export default {
  setup() {
    return {
      Trans
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
</style>