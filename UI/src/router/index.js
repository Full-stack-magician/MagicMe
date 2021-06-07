import Vue from 'vue'
import VueRouter from 'vue-router'
import ElementUI from 'element-ui'

import mainmenu from '../views/mainmenu'
import shiyangongneng from '../views/shiyangongneng'
import denglu from '../views/denglu'
import Home from '../views/Home'
import zhuce from '../views/zhuce'
import qiandao from '../views/qiandao'

Vue.use(VueRouter)

Vue.use(ElementUI)

const router = new VueRouter({
  routes: [
    {
      path: '/mainmenu',
      name: 'mainmenu',
      component: mainmenu
    },
    {
      path: '/shiyangongneng',
      name: 'shiyangongneng',
      component: shiyangongneng
    },
    {
      path: '/denglu',
      name: 'denglu',
      component: denglu
    },
    {
      path: '/Home',
      name: 'Home',
      component: Home
    },
    {
      path: '/zhucce',
      name: 'zhuce',
      component: zhuce
    },
    {
      path: '/qiandao',
      name: 'qiandao',
      component: qiandao
    }
  ]
})

export default router
