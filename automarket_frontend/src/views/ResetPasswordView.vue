<template>
    <form class="pt-14" @submit.prevent="submit">
      <h1 class="h3 mb-3 fw-normal">Please register</h1>

      <input v-model="data.password" type="password" class="form-control" placeholder="Password" required>
      <input v-model="data.password_confirm" type="password" class="form-control" placeholder="Password Confirm" required>
  
      <button class="w-100 btn btn-lg btn-primary" type="submit">Submit</button>
    </form>
  </template>
  
  <script>
  import {reactive} from 'vue';
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

        const submit = async () => {
        try {
          await axios.post('/api/reset/', data);

          console.log('Password reset email sent successfully!');
        } catch (error) {
          console.error('Error sending password reset email:', error.message);
        }
      };

        return {
            data,
            submit
        }
    }
  }
  </script>