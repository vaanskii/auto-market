<template>
  <form class="pt-20" @submit.prevent="submit">
    <h1 class="h3 mb-3 fw-normal">Please register</h1>

    <input
      autocomplete="email"
      id="email"
      v-model="data.email"
      type="email"
      class="form-control"
      placeholder="Email"
      required
    />

    <button class="w-100 btn btn-lg btn-primary" type="submit">Submit</button>
  </form>
</template>

<script>
import { reactive } from 'vue';
import axios from 'axios';

export default {
  name: 'Forgot',
  setup() {
    const data = reactive({
      email: '',
    });

    const submit = async () => {
      try {
        // Make a POST request to your Django API endpoint
        await axios.post('/api/forgot/', data);

        // Handle success (e.g., show a success message)
        console.log('Password reset email sent successfully!');
      } catch (error) {
        // Handle error (e.g., show an error message)
        console.error('Error sending password reset email:', error.message);
      }
    };

    return {
      data,
      submit,
    };
  },
};
</script>
