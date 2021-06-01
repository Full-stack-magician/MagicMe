import Vue from 'vue'
import Router from 'vue-router'
Vue.use(VueRouter)

import denglu from '../views/denglu.vue'
import Home from '../views/Home.vue'
import VueRouter from 'vue-router'
const routes=[
  {
    path:'/',
    name:'denglu',
    component:denglu
  },
  {
    path:'/Home',
    name:'Home',
    component:Home
  }
 
 
]
const router=new VueRouter({
  routes
})
const app = new Vue({
  router
}).$mount('#app')
export default router