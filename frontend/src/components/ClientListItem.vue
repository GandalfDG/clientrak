<script setup>
import { computed, ref } from '@vue/reactivity';

import ClientTimer from '@/components/ClientTimerButton.vue'

const props = defineProps(['tripData'])

const clientName = computed(() => {
    return ''.concat(props.tripData.client.client_first_name, ' ', props.tripData.client.client_last_name)
})

const tripName = ref(props.tripData.trip_name)
const timeSpent = ref(props.tripData.time_spent)

const commissionEstimate = 256.32

</script>

<template>
    <div class="box mb-2">
        <div class="level is-mobile">
            <div class="level-left">
                <div class="level-item">
                    <span class="icon is-medium"><i class="fas fa-caret-right fa-lg"></i></span>
                </div>
                <div class="level-item">
                    <h1>{{clientName}}'s <strong>{{tripName}}</strong> trip</h1>
                </div>
            </div>
            <div class="level-right">
                <div class="level-item">
                    <ClientTimer></ClientTimer>
                </div>
                <div class="level-item">
                    <span class="icon">
                        <i class="fas fa-edit fa-lg"></i>
                    </span>
                </div>
            </div>
        </div>
    </div>
</template>