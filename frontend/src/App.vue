<script setup>
import axios from 'axios'
import ClientListItem from '@/components/ClientListItem.vue'
import LoginForm from '@/components/LoginForm.vue'
import { onMounted } from 'vue';

const backendURL = import.meta.env.VITE_BACKEND_URL

</script>

<template>
    <h1 class="title">Backend URL: {{backendURL}}</h1>
    <section class="section">
        <LoginForm></LoginForm>
    </section>
    <section class="section">
        <ClientListItem></ClientListItem>
    </section>
</template>