import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'

import LoginView from '@/views/LoginView.vue'
import AgentView from '@/views/AgentView.vue'

import './assets/main.css'


const routes = [
    { path: '/', component: LoginView },
    { path: '/agent', component: AgentView}
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')

export default router
