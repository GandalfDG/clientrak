<script setup>
import LoginForm from '@/components/LoginForm.vue'

function loggedIn() {
    console.log("login successful")
}

</script>

<template>
    <LoginForm @logged-in="loggedIn()"></LoginForm>
</template>