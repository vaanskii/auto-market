import './assets/main.css'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import i18n from './i18n'
import axios from 'axios'
import { useUserStore } from '@/stores/user'

const originalWarn = console.warn;
console.warn = function (msg) {
  if (msg.includes('[intlify]')) {
    return;
  }
  originalWarn.apply(console, arguments);
};

axios.defaults.baseURL = 'https://vaanskii2.pythonanywhere.com'

const app = createApp(App)
const pinia = createPinia()

app.use(pinia)
app.use(router, axios)
app.use(i18n)

const userStore = useUserStore()
userStore.initStore()

app.mount('#app')