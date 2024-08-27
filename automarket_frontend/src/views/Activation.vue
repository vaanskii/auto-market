<template>
    <div class="md:pt-96 pt-14">
        <div class="flex justify-center text-center flex-col mb-96">
        <h2>Account Activation</h2>
        <p v-if="message">{{ message }}</p>
        </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import { onMounted, ref } from 'vue';
  
  export default {
    setup() {
      const message = ref('');
      const queryParams = new URLSearchParams(window.location.search);
      const email = queryParams.get('email');
      const userId = queryParams.get('id');
  
      onMounted(async () => {
        if (email && userId) {
          try {
            const response = await axios.get('/api/activateEmail/', {
              params: { email, id: userId }
            });
            message.value = response.data.message;
          } catch (error) {
            message.value = 'An error occurred. Please try again.';
          }
        } else {
          message.value = 'Invalid activation link.';
        }
      });
  
      return { message };
    }
  };
  </script>
  