<script setup>
import axios from 'axios'
import ClientListItem from '@/components/ClientListItem.vue'
import { onMounted } from 'vue';

const ax = axios.create({
  url: '/api',
  baseURL: 'http://localhost:1337'
})

onMounted(() => {

})

</script>

<template>
    <ClientListItem></ClientListItem>
</template>