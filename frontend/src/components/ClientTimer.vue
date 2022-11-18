<script setup>
import {ref} from 'vue'

const props = defineProps({
    tripData: {
        type: Object,
        required: true
    },
    agentData: {
        type: Object,
        required: true
    }
})

const paused = ref(true)

function togglePause() {
    paused.value = !paused.value
}

</script>

<template>
<div class="block">    
    <!-- timer -->
    <h1 class="title is-1">5:15:23</h1>
    <!-- commission visualization -->
    
    <!-- pause/resume button and stop/commit button -->
    <div class="field is-grouped is-grouped-centered">
        <div class="control">
            <!-- vue and vanilla font awesome don't play nice, might try vue-fontawesome if it's an issue -->
            <button class="button is-success is-light is-large" v-if="paused" @click="togglePause()">
                <span class="icon is-large">
                    <i class="fas fa-play"></i>
                </span>
            </button>
            <button class="button is-success is-light is-large" v-if="!paused" @click="togglePause()">
                <span class="icon is-large">
                    <i class="fas fa-pause"></i>
                </span>
            </button>
        </div>
        <div class="control">
            <button class="button is-success is-large">
                <span class="icon is-large">
                    <i class="fas fa-check"></i>
                </span>
            </button>
        </div>
    </div>
    
    <!-- activity selector dropdown -->
    <div class="field has-addons">
        <div class="control">
            <div class="select">
                <select>
                    <!-- agent's activity types will be stored in DB, allow adding a type -->
                    <option v-for="activity in agentData.activities">{{activity}}</option>
                </select>
            </div>
        </div>
        <div class="control">
            <button class="button is-primary">
                <span class="icon">
                    <i class="fas fa-plus"></i>
                </span>
            </button>
        </div>
    </div>
</div>
</template>