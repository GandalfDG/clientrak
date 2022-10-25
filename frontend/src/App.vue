<script setup>
import axios from 'axios'
import ClientListItem from '@/components/ClientListItem.vue'
import LoginForm from '@/components/LoginForm.vue'
import { onMounted } from 'vue';

const backendURL = import.meta.env.VITE_BACKEND_URL

function loggedIn() {
    console.log('logged in!')
}

</script>

<template>
    <h1 class="title">Backend URL: {{backendURL}}</h1>
    <section class="section">
        <LoginForm @logged-in="loggedIn"></LoginForm>
    </section>
    <section class="section">
        <ClientListItem></ClientListItem>
    </section>
</template>