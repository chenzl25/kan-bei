import Vue from 'vue'
import Router from 'vue-router'
import Entry from '@/components/Entry'
import Login from '@/components/Login'
import Register from '@/components/Register'
import Movie from '@/components/Movie'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Entry',
      component: Entry
    }, {
      path: '/login',
      name: 'Login',
      component: Login
    }, {
      path: '/register',
      name: 'Register',
      component: Register
    }, {
      path: '/movie/:movieId',
      name: 'Movie',
      component: Movie
    }
  ]
})
