<template>
  <div>
    <!-- Modal -->
    <div v-if="isOpen" class="fixed inset-0 z-50 overflow-auto bg-smoke-light flex">
      <div class="relative p-8 bg-white w-full max-w-md m-auto flex-col flex rounded-lg">
        <!-- Close Button -->
        <div class="flex justify-end">
          <button @click="closeModal" class="text-black">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
          </button>
        </div>
        <div class="flex flex-col justify-center items-center">
          <p class="text-center text-xl uppercase">Create or use an account to an add items</p>
          <div class="flex flex-row gap-4">
            <router-link :to="Trans.i18nRoute({ name: 'login' })" @click="onCloseModal()">
              <button class="uppercase mt-5 bg-black text-white rounded-lg py-3 px-2">login</button>
            </router-link>
            <router-link :to="Trans.i18nRoute({ name: 'signup' })" @click="onCloseModal()">
              <button class="uppercase mt-5 bg-black text-white rounded-lg py-3 px-2">Signup</button>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Trans from '@/i18n/translation'
import { RouterLink } from 'vue-router';
export default {
    setup() {
    return {
      Trans
    }
  },
  props: {
    isOpen: Boolean,
    onCloseModal: Function,
  },
  methods: {
    closeModal() {
        this.onCloseModal()
    }
  }
};
</script>

<style>
.bg-smoke-light {
  background-color: rgba(0, 0, 0, 0.5);
}
</style>
