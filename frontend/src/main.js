import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'

import LoginView from '@/views/LoginView.vue'

import './assets/main.css'


const routes = [
    { path: '/', component: LoginView }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
