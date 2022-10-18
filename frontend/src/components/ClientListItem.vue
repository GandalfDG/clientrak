<script setup>
import { computed } from '@vue/reactivity';


const clientName = "John Doe"
const tripName = "Disney World"
const commissionEstimate = 256.32
const timeSpent = 18 * 60 * 60 + 275

const timeDisplay = computed(() => {
    const hours = (Math.floor(timeSpent / 3600)).toString()
    const minutes = (Math.floor((timeSpent % 3600) / 60)).toString()
    
    const paddedMinutes = minutes.length < 2 ? '0' + minutes : minutes
    return ' '.concat(hours, ':', paddedMinutes)
})

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
                    <button class="button is-success">
                    <span class="icon-text">
                        <span class="icon">
                            <i class="far fa-clock"></i>
                        </span>
                        <h1>{{ timeDisplay }}</h1>
                        <span class="icon">
                            <i class="fas fa-pause"></i>
                        </span>
                    </span>
                    </button>
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