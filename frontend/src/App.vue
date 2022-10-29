<script setup>
import axios from 'axios'
import ClientListItem from '@/components/ClientListItem.vue'
import LoginForm from '@/components/LoginForm.vue'
import { onMounted } from 'vue';
import { RouterView } from 'vue-router'

import NavBar from '@/components/NavBar.vue'

const backendURL = import.meta.env.VITE_BACKEND_URL

function isLoggedIn() {

}

function loggedIn() {
    console.log('logged in!')
}

</script>

<template>
    <NavBar></NavBar>
    <RouterView></RouterView>
</template>