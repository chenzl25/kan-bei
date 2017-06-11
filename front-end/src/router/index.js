import Vue from 'vue'
import Router from 'vue-router'
import Entry from '@/components/Entry'
import Login from '@/components/Login'
import Register from '@/components/Register'
import Movie from '@/components/Movie'
import Buy from '@/components/Buy'
import Site from '@/components/Site'

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
    }, {
      path: '/buy/:movieId',
      name: 'Buy',
      component: Buy
    }, {
      path: '/site/:movieId/:cinemaId/:price',
      name: 'Site',
      component: Site
    }
  ]
})
