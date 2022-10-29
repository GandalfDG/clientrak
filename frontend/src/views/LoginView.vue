<script setup>
import LoginForm from '@/components/LoginForm.vue'

function loggedIn() {

}

</script>

<template>
    <LoginForm @logged-in="loggedIn()"></LoginForm>
</template>