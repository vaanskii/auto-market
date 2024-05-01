<template>
  <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto h-screen lg:py-0">
      <div class="w-full p-6 bg-[#222] rounded-lg shadow dark:border md:mt-0 sm:max-w-md  sm:p-8">
          <h1 class="mb-1 text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
              Forgot your password?
          </h1>
          <p class="font-light text-white">Don't fret! Just type in your email and we will send you a code to reset your password!</p>
          <form  @submit.prevent="submit" class="mt-4 space-y-4 lg:mt-5 md:space-y-5">
              <div>
                  <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">New Password</label>
                  <input 
                  v-model="data.password" 
                    type="password" 
                    name="password" 
                    autocomplete="password"
                    id="email" 
                    class="bg-gray-50 border border-white placeholder:text-black text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 " 
                    placeholder="*********" 
                    required
                  >
              </div>
              <div>
                <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Confirm New Password</label>
                  <input 
                  v-model="data.password_confirm" 
                    type="password" 
                    name="password" 
                    autocomplete="password"
                    id="email" 
                    class="bg-gray-50 border border-white placeholder:text-black text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 " 
                    placeholder="*********" 
                    required
                  >
              </div>
              <button 
                    class="btn2 w-full mt-10 px-10 py-5 text-lg relative transition-colors border border-white rounded-md uppercase font-semibold tracking-wider leading-none overflow-hidden hover:text-white" 
                    type="submit"
                    >
                    <span class="absolute inset-0 bg-white"></span>
                    <span class="absolute inset-0 flex text-white justify-center hover:text-black items-center font-bold">Confirm password</span>
                </button>
                <transition name="fade" mode="out-in">
                <div v-if="submitSuccessfully" key="confirmation" id="toast-simple" class="flex mt-4  items-center w-full p-4 space-x-4 rtl:space-x-reverse text-black uppercase bg-green-300 rounded-lg shadow-2xl" role="alert">
                    <svg class="w-8 h-8 text-black rotate-45" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 20">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m9 17 8 2L9 1 1 19l8-2Zm0 0V9"/>
                    </svg>
                    <p class="ps-4 text-sm font-normal">Password changed successfully. You can login now</p>
                </div>
              </transition>
          </form>
      </div>
  </div>
</template>
  
  <script>
  import {reactive, ref, onMounted} from 'vue';
  import { useRoute } from 'vue-router';
  import axios from 'axios'
  export default {
    name: "Register",
    setup() {
        const route = useRoute()
        const data = reactive({
            token: route.params.token,
            password: '',
            password_confirm: ''
        })

        const submitSuccessfully = ref(false);

        const submit = async () => {
        try {
          await axios.post('/api/reset/', data);
          submitSuccessfully.value = true
          setTimeout(() => {
              submitSuccessfully.value = false;
            }, 5000);
          } catch (error) {
            console.error('Error sending password reset email:', error.message);
          }
        };
        onMounted(() => {
          document.title = 'Reset Password';
        });
        return {
            data,
            submit,
            submitSuccessfully
        }
    }
  }
  </script>