<script setup>
import Timer from '@/components/ClientTimer.vue'

const dummyClientData = {
    "trip_name": "asdf",
    "commission": "2584.30",
    "time_spent": 0,
    "client": {
        "client_first_name": "Jack",
        "client_last_name": "Case",
        "agent": 2
    },
    "id": 1
}

</script>

<template>
    <Timer :trip-data="dummyClientData"></Timer>
</template>