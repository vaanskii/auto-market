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
          {{ $t('changeinfo.paragraph') }}
        </p>
        <p class="flex flex-col items-center justify-center mt-10 text-center">
            <span>{{ $t('changeinfo.password') }}</span>
            <router-link :to="Trans.i18nRoute({ name: 'password', params: {'id': userStore.user.id} })" class="underline mt-px">{{ $t('changeinfo.getstart') }}</router-link>
          </p>
        <p class="mt-6 text-sm text-center text-gray-300">
          Read our <a href="#" class="underline">terms</a> and <a href="#" class="underline">conditions</a>
        </p>
      </div>
      <div class="p-5 bg-[#E6E6E6] md:flex-1">
        <h3 class="my-4 text-2xl font-semibold text-gray-700 uppercase">{{  $t('changeinfo.header')  }}</h3>
        <form v-on:submit.prevent="submitForm" action="#" class="flex flex-col space-y-5">
          <div class="flex flex-col space-y-1">
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
          </div>
          <!-- Mobile number and country code -->
          <div class="group w-full">
            <label for="tel" class="text-sm font-semibold text-gray-500">{{ $t('changeinfo.mobile_number') }}</label>
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
                  <span class="absolute inset-0 flex justify-center items-center font-bold">{{ $t('changeinfo.save') }}</span>
              </button>
          </div>
          <template v-if="errors.length > 0">
              <div class="bg-red-300 text-white rounded-lg p-6">
                  <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
              </div>
          </template>
        </form>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
import axios from 'axios'
import { useUserStore } from '@/stores/user'
import { RouterLink } from 'vue-router'
import Trans from '@/i18n/translation'
import { computed, watch, onMounted } from 'vue';
export default{
setup() {
  const userStore = useUserStore()
  const pageTitle = computed(() => `Settings of ${userStore.user.name}`);

  watch(pageTitle, (newTitle) => {
    document.title = newTitle;
  }, { immediate: true });
  return {
      pageTitle,
      userStore,
      Trans
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
        if(response.data.message === 'profile uploaded successfully'){
          this.userStore.setUserInfo({
            id: this.userStore.user.id,
            name: this.form.name,
            email: this.form.email,
            mobile_number: fullMobileNumber,
            country_code: this.form.country_code
          })
          this.$router.back()
        }else{
          this.errors.push(response.data.message)
        }
      })
      .catch(error => {
        console.log('An error occurred: ', error)
      })
    }
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