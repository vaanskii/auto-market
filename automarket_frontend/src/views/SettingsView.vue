<template>
  <div class="pt-14">
      <form v-on:submit.prevent="submitForm" action="#" class="flex flex-col space-y-5">
          <div class="flex flex-col space-y-1">
            <label for="email" class="text-sm font-semibold text-gray-500">Email address</label>
            <input
              type="email"
              id="email"
              autofocus
              v-model="form.email"
              placeholder="Enter your mail"
              class="px-4 py-2 transition duration-300 border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black"
              autocomplete="email"
            />
          </div>
          <div class="flex flex-col space-y-1">
            <label for="name" class="text-sm font-semibold text-gray-500">Name</label>
            <input
              type="text"
              id="name"
              autofocus
              v-model="form.name"
              placeholder="Enter your name"
              class="px-4 py-2 transition duration-300 border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black"
              autocomplete="email"
            />
          </div>
          <!-- Mobile number and country code -->
          <div class="group w-full">
            <label for="tel" class="text-sm font-semibold text-gray-500">Mobile Number</label>
            <div class="relative flex items-center">
              <input
                  type="tel"
                  id="tel"
                  autofocus
                  v-model="form.mobile_number"
                  placeholder="Mobile number"
                  class="peer relative h-10 w-full rounded-md bg-gray-50 pl-32 pr-4 outline-none"
                  autocomplete="tel"
              />
              <select v-model="form.country_code" id="country_code" class="absolute text-center h-10 w-28 outline-none rounded-l-md text-sm bg-[#222] font-semibold text-white ">
                  <option value="+995">Geo (+995)</option>
                  <option value="+1">USA (+1)</option>
              </select>
            </div>
          </div>
          <div>
              <button 
                  class="btn2 w-full mt-10 px-10 py-5 text-lg relative transition-colors border border-black rounded-md uppercase font-semibold tracking-wider leading-none overflow-hidden hover:text-white" 
                  type="submit"
                  >
                  <span class="absolute inset-0 bg-[#222]"></span>
                  <span class="absolute inset-0 flex justify-center items-center font-bold">save</span>
              </button>
          </div>
          <template v-if="errors.length > 0">
              <div class="bg-red-300 text-white rounded-lg p-6">
                  <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
              </div>
          </template>
        </form>
  </div>
</template>

<script>
import axios from 'axios'
import { useUserStore } from '@/stores/user'
import { RouterLink } from 'vue-router'
export default{
setup() {
  const userStore = useUserStore()
  return {
      userStore
  }
},
data() {
  return {
      form: {
          name: this.userStore.user.name,
          email: this.userStore.user.email,
          mobile_number: this.userStore.user.mobile_number,
          country_code: this.userStore.user.country_code
      },
      errors: []
  }
},
methods: {
submitForm() {
this.errors = []

if(this.form.name === ''){
  this.errors.push('Your name is missing!')
}
if(this.form.email === ''){
  this.errors.push('Your email is missing!')
}
if(this.form.mobile_number === ''){
  this.errors.push('Your mobile number is missing!')
}
if(this.errors.length === 0){
  const fullMobileNumber = this.form.country_code + this.form.mobile_number
  const payload = {
    ...this.form,
    mobile_number: fullMobileNumber
  }

  axios.post('/api/editprofile/', payload)
    .then(response => {
      console.log('Profile updated successfully', response.data)
      this.userStore.setUserInfo({
        id: this.userStore.user.id,
        name: this.form.name,
        email: this.form.email,
        mobile_number: fullMobileNumber,
        country_code: this.form.country_code
      })
      this.$router.back()
    })
    .catch(error => {
      console.log('An error occurred: ', error)
    })
}
} 
}
}
</script>