<template>
  <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto h-screen lg:py-0">
      <div class="w-full p-6 bg-[#222] rounded-lg shadow dark:border md:mt-0 sm:max-w-md  sm:p-8">
          <h1 class="mb-1 text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
              Forgot your password?
          </h1>
          <p class="font-light text-white">Don't fret! Just type in your email and we will send you a code to reset your password!</p>
          <form  @submit.prevent="submit" class="mt-4 space-y-4 lg:mt-5 md:space-y-5">
              <div>
                  <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your email</label>
                  <input 
                    v-model="data.email" 
                    type="email" 
                    name="email" 
                    autocomplete="email"
                    id="email" 
                    class="bg-gray-50 border border-white placeholder:text-black text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 " 
                    placeholder="name@company.com" 
                    required
                  >
              </div>
              <div class="flex items-start">
                  <div class="flex items-center h-5">
                    <input id="terms" aria-describedby="terms" type="checkbox" class="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800" required="">
                  </div>
                  <div class="ml-3 text-sm">
                    <label for="terms" class="font-light text-gray-500 dark:text-gray-300">I accept the <a class="font-medium text-primary-600 hover:underline dark:text-primary-500" href="#">Terms and Conditions</a></label>
                  </div>
              </div>
              <button 
                    class="btn2 w-full mt-10 px-10 py-5 text-lg relative transition-colors border border-white rounded-md uppercase font-semibold tracking-wider leading-none overflow-hidden hover:text-white" 
                    type="submit"
                    >
                    <span class="absolute inset-0 bg-white"></span>
                    <span class="absolute inset-0 flex text-white justify-center hover:text-black items-center font-bold">Reset password</span>
                </button>
                <transition name="fade" mode="out-in">
                <div v-if="submitSuccessfully" key="confirmation" id="toast-simple" class="flex mt-4  items-center w-full p-4 space-x-4 rtl:space-x-reverse text-black uppercase bg-green-300 rounded-lg shadow-2xl" role="alert">
                    <svg class="w-8 h-8 text-black rotate-45" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 20">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m9 17 8 2L9 1 1 19l8-2Zm0 0V9"/>
                    </svg>
                    <p class="ps-4 text-sm font-normal">We've sent a confirmation message to your email. Please check your inbox.</p>
                </div>
              </transition>
          </form>
      </div>
  </div>
</template>

<script>
import { reactive, ref } from 'vue';
import axios from 'axios';

export default {
  name: 'Forgot',
  setup() {
    const data = reactive({
      email: '',
    });
    const submitSuccessfully = ref(false);

    const submit = async () => {
      try {
        await axios.post('/api/forgot/', data);
        data.email = '',
        submitSuccessfully.value = true
        setTimeout(() => {
          submitSuccessfully.value = false;
        }, 5000);
        console.log('Password reset email sent successfully!');
      } catch (error) {
        console.error('Error sending password reset email:', error.message);
      }
    };

    return {
      data,
      submit,
      submitSuccessfully
    };
  },
};
</script>

<style>
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