import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SobreView from '../views/SobreView.vue'
import ObrasView from '../views/ObrasView.vue'
import ContatosView from '../views/ContatosView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/sobre',
    name: 'sobre',
    component: SobreView
  },
  {
    path: '/obras',
    name: 'obras',
    component: ObrasView
  },
  {
    path: '/eventos',
    name: 'eventos',
    component: ObrasView
  },
  {
    path: '/contatos',
    name: 'contatos',
    component: ContatosView
  },
  
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
