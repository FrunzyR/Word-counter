<template>
    <LiteYouTubeEmbed :id="videoStore.videoId" title="something?"/>
</template>

<script setup lang="ts">
import { useVideoStore } from '@/stores/video';
import LiteYouTubeEmbed from 'vue-lite-youtube-embed'
import 'vue-lite-youtube-embed/style.css'

const props = defineProps<{
    videoURL?: string
}>();

const videoStore = useVideoStore()
</script>

<style scoped>
iframe {
    width: 100%;
    height: 40vh;
}
</style>