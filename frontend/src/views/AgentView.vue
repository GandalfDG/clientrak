<script setup>
import axios from 'axios';
import ClientListItem from '@/components/ClientListItem.vue'
import { onMounted, reactive } from 'vue';

const backendURL = import.meta.env.VITE_BACKEND_URL

onMounted(() => {
    getAgentTrips()
})

const tripData = reactive({})

function getAgentTrips() {
    axios({
        url: '/api/trips/',
        method: 'get',

        baseURL: backendURL,
        headers: {'Authorization': ''.concat('Token ', window.sessionStorage.getItem('authtoken'))}
    }).then((response)=> {
        tripData.value = response.data
        console.log(response.data)
    })
}

</script>

<template>
    <ClientListItem v-for="trip in tripData.value" :trip-data="trip"></ClientListItem>
</template>