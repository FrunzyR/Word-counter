<template>
    <div class="container">
        <div class="first-column">
            <h1>{{ body.videoTitle }}</h1>
            <VideoPreview />
        </div>

        <div class="second-column">
            <DataTable :value="body.results" tableStyle="min-width: 50rem">
                <Column field="word" header="Word"></Column>
                <Column field="count" header="Count"></Column>
            </DataTable>
        </div>
    </div>
</template>

<script setup lang="ts">
import { useVideoStore } from '@/stores/video';
import VideoPreview from '@/components/VideoPreview.vue';

const videoStore = useVideoStore()

const response = await fetch("/api/analyse?" + new URLSearchParams({
    videoId: videoStore.videoId,
    lang: "en"
}));
const body = await response.json()
console.log(body)
</script>

<style scoped>
.container {
    height: inherit;

    display: flex;
    font-size: large;
}

.first-column {
    width: 50%;
    display: flex;
    flex-direction: column;
    justify-content: start;
    font-weight: bold;
    padding: 2%;
}

h1 {
    font-size: 60px;
    margin: 0 0 50px 0;
}

.second-column {
    width: 50%;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
}
</style>
