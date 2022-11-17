<script setup>
import { computed, ref } from 'vue'
/* receive the currently spent time from the server in serverTime prop
 * when clicked, start counting up. When clicked again, pause and post
 * new spent time to the server
 */
const props = defineProps(['serverTime'])

let timeSpent = {value:3589}

let isTiming = ref(false)

const timeDisplay = computed(() => {
    const hours = (Math.floor(timeSpent.value / 3600)).toString()
    const minutes = (Math.floor((timeSpent.value % 3600) / 60)).toString()

    const paddedMinutes = minutes.length < 2 ? '0' + minutes : minutes
    return ' '.concat(hours, ':', paddedMinutes)
})

function toggleTimer() {
    isTiming.value = !isTiming.value
    console.log(isTiming.value)
}

function startTiming() {
    // set an interval, increment time spent each second
}

function stopTiming() {
    // clear the interval, post the new total time spent to the server
    // TODO maybe make a POST route that just takes a number of seconds so the DB handles atomicity?
    // probably not a problem for now

}

</script>

<template>
    <button class="button is-success" @click="toggleTimer()">
        <span class="icon-text">
            <span class="icon">
                <i class="far fa-clock"></i>
            </span>
            <h1>{{ timeDisplay }}</h1>
            <span class="icon">
                <i class="fas fa-play"></i>
            </span>
        </span>
    </button>
</template>