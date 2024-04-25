import { defineStore } from 'pinia'
import axios from 'axios'

export const useUserStore = defineStore({
    id: 'user',

    state: () => ({
        user: {
            isAuthenticated: false,
            id: null,
            email: null,
            name: null,
            mobile_number: null,
            access: null,
            refresh: null,
            country_code: null
        }
    }),

    actions: {
        initStore() {
            if (localStorage.getItem('user.access')) {
                this.user.access = localStorage.getItem('user.access')
                this.user.refresh = localStorage.getItem('user.refresh')
                this.user.id = localStorage.getItem('user.id')
                this.user.name = localStorage.getItem('user.name')
                this.user.email = localStorage.getItem('user.email')
                this.user.mobile_number = localStorage.getItem('user.mobile_number')
                this.user.country_code = localStorage.getItem('user.country_code')
                this.user.isAuthenticated = true

                axios.defaults.headers.common["Authorization"] = "Bearer " + this.user.access;

                this.refreshToken()
            }
        },

        setToken(data) {
            this.user.access = data.access
            this.user.refresh = data.refresh
            this.user.isAuthenticated = true

            localStorage.setItem('user.access', data.access)
            localStorage.setItem('user.refresh', data.refresh)
        },

        removeToken() {
            this.user.refresh = null
            this.user.access = null
            this.user.isAuthenticated = false
            this.user.id = null
            this.user.name = null
            this.user.mobile_number = null
            this.user.email = null
            this.country_code = null

            localStorage.setItem('user.access', '')
            localStorage.setItem('user.refresh', '')
            localStorage.setItem('user.id', '')
            localStorage.setItem('user.name', '')
            localStorage.setItem('user.mobile_number', '')
            localStorage.setItem('user.email', '')
            localStorage.setItem('user.country_code', '')
        },

        setUserInfo(user) {
            const mobileNumberWithoutCountryCode = this.removeCountryCode(user.mobile_number, user.country_code);

            this.user.id = user.id
            this.user.name = user.name
            this.user.email = user.email
            this.user.mobile_number = mobileNumberWithoutCountryCode
            this.user.country_code = user.country_code

            localStorage.setItem('user.id', this.user.id)
            localStorage.setItem('user.name', this.user.name)
            localStorage.setItem('user.email', this.user.email)
            localStorage.setItem('user.mobile_number', this.user.mobile_number)
            localStorage.setItem('user.country_code', this.user.country_code)
        },

        removeCountryCode(mobileNumber, countryCode) {
            if (mobileNumber.startsWith(countryCode)) {
                return mobileNumber.slice(countryCode.length);
            }
            return mobileNumber;
        },

        refreshToken() {
            axios.post('/api/refresh/', {
                refresh: this.user.refresh
            })
                .then((response) => {
                    this.user.access = response.data.access

                    localStorage.setItem('user.access', response.data.access)

                    axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access
                })
                .catch((error)=>{
                    console.log(error)
                    this.removeToken()
                })
        },
    }
})