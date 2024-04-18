import './assets/main.css'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import i18n from './i18n'
import axios from 'axios'
import { useUserStore } from '@/stores/user' // Import your user store

axios.defaults.baseURL = "http://127.0.0.1:8000"

const app = createApp(App)
const pinia = createPinia()

app.use(pinia)
app.use(router, axios)
app.use(i18n)

// Initialize the user store and load the user's authentication state
const userStore = useUserStore()
userStore.initStore()

app.mount('#app')
