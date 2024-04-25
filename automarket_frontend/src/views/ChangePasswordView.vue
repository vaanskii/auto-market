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
            {{ $t('changepassword.paragraph') }}
          </p>
          <p class="flex flex-col items-center justify-center mt-10 text-center">
            <span>{{ $t('changepassword.info') }}</span>
            <router-link :to="Trans.i18nRoute({ name: 'settings', params: {'id': userStore.user.id} })" class="underline mt-px">{{ $t('changeinfo.getstart') }}</router-link>
          </p>
          <p class="mt-6 text-sm text-center text-gray-300">
            Read our <a href="#" class="underline">terms</a> and <a href="#" class="underline">conditions</a>
          </p>
        </div>
        <div class="p-5 bg-[#E6E6E6] md:flex-1">
          <h3 class="my-4 text-2xl font-semibold text-gray-700 uppercase">{{ $t('changepassword.header') }}</h3>
          <form v-on:submit.prevent="changePassword" action="#" class="flex flex-col space-y-5">
            <input hidden type="text" autocomplete="username" value="" id="hidden-username">
            <div class="flex flex-col space-y-1">
              <div class="flex items-center justify-between">
                <label for="old_password" class="text-sm font-semibold text-gray-500">{{ $t('changepassword.old_password') }}</label>
              </div>
              <input
                type="password"
                id="old_password"
                placeholder="*********"
                v-model="form.old_password"
                class="px-4 py-2 transition duration-300 border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black"
                autocomplete="current-password"
              />
            </div>
            <div class="flex flex-col space-y-1">
              <div class="flex items-center justify-between">
                <label for="new_password1" class="text-sm font-semibold text-gray-500">{{ $t('changepassword.new_password1') }}</label>
              </div>
              <input
                type="password"
                id="new_password1"
                placeholder="*********"
                v-model="form.new_password1"
                class="px-4 py-2 transition duration-300 border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black"
                autocomplete="current-password"
              />
            </div>
            <div class="flex flex-col space-y-1">
              <div class="flex items-center justify-between">
                <label for="new_password2" class="text-sm font-semibold text-gray-500">{{ $t('changepassword.new_password2') }}</label>
              </div>
              <input
                type="password"
                id="new_password2"
                v-model="form.new_password2"
                placeholder="*********"
                class="px-4 py-2 transition duration-300 border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black"
                autocomplete="current-password"
              />
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
import axios from 'axios';
import { useUserStore } from '@/stores/user';
import Trans from '@/i18n/translation';
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
          old_password: '',
          new_password1: '',
          new_password2: ''
        },
        errors: []
      }
  },
  methods: {
    changePassword() {
      axios
        .post('/api/changepassword/', this.form)
        .then(response => {
          if (response.data.message === 'success'){
            this.$router.back()
            this.$router.back()
          }
        })
        .catch(error => {
          console.log(error)
        })
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