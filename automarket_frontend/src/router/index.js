import { createRouter, createWebHistory, RouterView } from 'vue-router'
import Trans from '@/i18n/translation'
import HomeView from '../views/HomeView.vue'
import CarView from '../views/CarsView.vue'
import Login from '../views/Login.vue'
import Signup from '../views/Signup.vue'
import Add from '../views/Add.vue'
import Blogs from '../views/BlogsView.vue'
import Search from '../views/SearchView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/:locale?",
      component: RouterView,
      beforeEnter: Trans.routeMiddleware,
      children: [
        {
          path: '',
          name: 'home',
          component: HomeView
        },
        {
          path: 'about',
          name: 'about',
          component: CarView
        },
        {
          path: 'login',
          name: 'login',
          component: Login
        },
        {
          path: 'signup',
          name: 'signup',
          component: Signup
        },
        {
          path: 'add',
          name: 'add',
          component: Add
        },
        {
          path: 'blogs',
          name: 'blogs',
          component: Blogs,
          beforeEnter: (to, from, next) => {
            // Scroll to the top of the page
            window.scrollTo(0, 0);
            next();
          }
        },
        {
          path: 'search',
          name: 'search',
          component: Search,
          },
      ]
    }
  ],
});

export default router
