import './assets/main.css'
import { createApp } from 'vue'
// import { createApp } from 'vue/dist/vue.esm-bundler'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import i18n from './i18n'
import axios from 'axios'

axios.defaults.baseURL = "http://127.0.0.1:8000"

const app = createApp(App)
app.use(createPinia())
app.use(router, axios)
app.use(i18n)

app.mount('#app')
