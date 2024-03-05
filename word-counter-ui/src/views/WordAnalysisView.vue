<template>
    <div class="container grid">
        <div class="first-column col-12 md:col-6">
            <h1>{{ body.videoTitle }}</h1>
            <VideoPreview />
        </div>

        <div class="second-column col-12 md:col-6">
            <DataTable :value="body.results">
                <Column header="Top" headerStyle="width:3rem">
                    <template #body="slotProps">
                         {{ slotProps.index + 1 }}
                    </template>
                 </Column>
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
    font-size: large;
}

.first-column {
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
    display: flex;
    flex-direction: column;
    justify-content: space-around;
}
</style>
