<template>
    <LiteYouTubeEmbed :id="youtube_parser(videoURL)" title="something?"/>
</template>

<script setup lang="ts">
import LiteYouTubeEmbed from 'vue-lite-youtube-embed'
import 'vue-lite-youtube-embed/style.css'

const props = defineProps<{
    videoURL: string
}>();

function youtube_parser(url: string): string{
    if(!url) return "lADBHDg-JtA";

    var regExp = /^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*/;
    var match = url.match(regExp);
    return (match&&match[7].length==11)? match[7] : "";
}

</script>

<style scoped>
iframe {
    width: 100%;
    height: 40vh;
}
</style>