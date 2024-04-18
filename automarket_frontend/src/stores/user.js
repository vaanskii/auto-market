import { defineStore } from "pinia";
import axios from "axios";
import { M } from "vite/dist/node/types.d-aGj9QkWt";

export const useUserStore = defineStore({
    id: "user",

    state: () => ({
        user:{
            isAuthenticated: false,
            id: null,
            email: null,
            name: null,
            mobile_number: null,
            access: null,
            refresh: null
        }
    }),

    actions: {
        initStore() {
            if(localStorage.getItem('user.access')) {
                this.user.id = localStorage.getItem('user.id')
                this.user.access = localStorage.getItem('user.access')
                this.user.refresh = localStorage.getItem('user.refresh')
                this.user.email = localStorage.getItem('user.email')
                this.user.name = localStorage.getItem('user.name')
                this.user.mobile_number = localStorage.getItem('user.mobile_number')
                this.user.isAuthenticated = true

                this.refreshToken()
            }
        },

        refreshToken() {
            axios.post('api/refresh/', {
                refresh: this.user.refresh
            }).then((response) => {
                this.user.access = response.data.access
                localStorage.setItem('user.access', response.data.access)
                axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access
            }).catch((error) => {
                console.log(error)
                this.removeToken()
            })
        },
        setToken(data) {
            this.user.access = data.access
            this.user.refresh = data.refresh
            this.user.isAuthenticated = true

            localStorage.setItem('user.access', data.access)
            localStorage.setItem('user.refresh', data.refresh)
        },
        setUserInfo(user) {
            this.user.id = user.id
            this.user.name = user.name
            this.user.email = user.email
            this.user.mobile_number = user.mobile_number

            localStorage.setItem('user.id', this.user.id)
            localStorage.setItem('user.username', this.user.username)
            localStorage.setItem('user.email', this.user.email)
            localStorage.setItem('user.mobile_number', this.user.mobile_number)

        },
        removeToken() {
            this.user.id = null
            this.user.refresh = null
            this.user.access = null
            this.user.name = null
            this.user.email = null
            this.user.mobile_number = null
            this.user.isAuthenticated = false

            localStorage.setItem('user.access', '')
            localStorage.setItem('user.refresh', '')
            localStorage.setItem('user.id', '')
            localStorage.setItem('user.name', '')
            localStorage.setItem('user.email', '')
            localStorage.setItem('user.mobile_number', '')
        },
    }
})