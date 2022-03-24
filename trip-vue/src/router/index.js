import Vue from 'vue'
import VueRouter from 'vue-router'


Vue.use(VueRouter)

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)
}

const routes = [
  {
    path:'/login',
    name:'login',
    component: () => import('views/Login')
  },
  {
    path: '/',
    name: 'Home',
    component: () => import('views/Home/Home')
  },
  {
    path:'/vlog',
    name:'Vlog',
    component: () => import('views/Vlog/Vlog')
  },
  {
    path:'/chatrecommend',
    name:'ChatRecommend',
    component: () => import('views/ChatRecommend/ChatRecommend')
  },
  {
    path:'/creation',
    name:'Creation',
    component: () => import('views/Creation/Creation')
  },
  {
    path:'/travelnote',
    name:'TravelNote',
    component: () => import('views/TravelNote/TravelNote'),
  },
  {
    path:'/detail/:local',
    name:'Detail',
    component: () => import('views/TravelNote/Detail')
  },
  {
    path:'/vip',
    name:'Vip',
    component: () => import('views/VIP/vip')
  }
]

const router = new VueRouter({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes,
  scrollBehavior(to, from, savedPosition) {
    return { x: 0, y: 0 };
  },
})

export default router
