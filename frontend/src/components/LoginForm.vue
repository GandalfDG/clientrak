<script setup>
import axios from 'axios'
import { ref } from 'vue'

const backendURL = import.meta.env.VITE_BACKEND_URL

const emit = defineEmits(['loggedIn'])

const emailField = ref(null)
const passwordField = ref(null)

function submitLogin() {
    axios({
        method: 'post',
        baseURL: backendURL,
        url: '/api/token_auth/',
        data: {
            username: emailField.value,
            password: passwordField.value
        }
    }).then((response) => {
        if (response.status === 200) {
            window.sessionStorage.setItem('authtoken', response.data.token)
            emit('loggedIn')
        }
    })
}
</script>

<template>
    <div class="box">
        <h1 class="title is-3 mb-4">Login</h1>
        <div class="field">
            <p class="control has-icons-left">
                <input class="input" type="email" v-model="emailField" placeholder="Email">
                <span class="icon is-small is-left">
                    <i class="fas fa-envelope"></i>
                </span>
            </p>
        </div>
        <div class="field">
            <p class="control has-icons-left">
                <input class="input" type="password" v-model="passwordField" placeholder="Password">
                <span class="icon is-small is-left">
                    <i class="fas fa-key"></i>
                </span>
            </p>
        </div>
        <div class="field is-grouped is-grouped-right">
            <button class="button is-primary" @click="submitLogin()">
                <p>Submit</p> <span class="icon">
                    <i class="fas fa-arrow-right"></i>
                </span>
            </button>
        </div>
    </div>
</template>