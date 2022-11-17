<script setup>
import {ref} from 'vue'

const props = defineProps({
    tripData: {
        type: Object,
        required: true
    }
})

const paused = ref('true')

</script>

<template>
<!-- timer -->
<h1 class="title is-1">5:15:23</h1>
<!-- commission visualization -->
<!-- pause/resume button and stop/commit button -->
</template>