import { createRouter, createWebHistory, RouterView } from 'vue-router'
import Trans from '@/i18n/translation'
import HomeView from '../views/HomeView.vue'
import CarView from '../views/CarsView.vue'
import Login from '../views/LoginView.vue'
import Signup from '../views/SignupView.vue'
import Add from '../views/AddView.vue'
import Blogs from '../views/BlogsView.vue'
import Search from '../views/SearchView.vue'
import Settings from '../views/SettingsView.vue'
import Password from '../views/ChangePasswordView.vue'
import Profile from '../views/ProfileView.vue'
import Vin from '../views/VinResultsView.vue'
import Forgot from '../views/ForgotPasswordView.vue'
import Reset from '../views/ResetPasswordView.vue'

import { useUserStore } from '@/stores/user'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else if (to.hash) {
      return { selector: to.hash, behavior: 'smooth' }
    } else {
      return { left: 0, top: 0, behavior: 'smooth' }
    }
  },
  routes: [
    {
      path: "/:locale?",
      component: RouterView,
      beforeEnter: Trans.routeMiddleware,
      children: [
        {
          path: '',
          name: 'home',
          component: HomeView,
        },
        {
          path: 'car/:id',
          name: 'cardetail',
          component: CarView
        },
        {
          path: 'login',
          name: 'login',
          component: Login,
          beforeEnter: (to, from, next) => {
            const userStore = useUserStore()
            if (userStore.user.isAuthenticated) {
              next({ name: 'home' })
            } else {
              next();
            } 
          }
        },
        {
          path: 'signup',
          name: 'signup',
          component: Signup,
          beforeEnter: (to, from, next) => {
            const userStore = useUserStore()
            if (userStore.user.isAuthenticated) {
              next({ name: 'home' })
            } else {
              next();
            } 
          }
        },
        {
          path: 'add',
          name: 'add',
          component: Add,
          beforeEnter: (to, from, next) => {
            const userStore = useUserStore()
            if (!userStore.user.isAuthenticated) {
              next({ name: 'home' })
            } else {
              next();
            } 
          }
        },
        {
          path: 'settings/:id',
          name: 'settings',
          component: Settings
        },
        {
          path: 'password/:id',
          name: 'password',
          component: Password
        },
        {
          path: 'profile/:id',
          name: 'profile',
          component: Profile
        },
        {
          path: 'blogs',
          name: 'blogs',
          component: Blogs,
        },
        {
          path: 'search',
          name: 'search',
          component: Search,
        },
        {
          path: 'vin',
          name: 'vin',
          component: Vin,
        },
        {
          path: 'forgot',
          name: 'forgot',
          component: Forgot,
        },
        {
          path: 'reset/:token',
          name: 'reset',
          component: Reset,
        }
      ]
    }
  ],
});

export default router
