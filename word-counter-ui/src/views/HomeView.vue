<template>
    <div class="container grid">
        <div class="first-column col-12 md:col-6">
            <h1>Youtube caption word counter</h1>
            <!-- <div class="flex flex-column gap-2">
                <label for="selectedOption">Select content type</label>
                <Dropdown id="selectedOption" v-model="selectedOption" :options="options" optionLabel="name" class="w-full" />
            </div> -->
            <div class="flex flex-column gap-2">
                <label for="url">Paste the link of a {{ selectedOption.name }}</label>
                <InputText id="url" v-model="videoURLInput" placeholder="Your URL"/>
            </div>
            <hr>
            <Button label="Analyse" :disabled="!videoURLInput" @click="$router.push('analysis')"/>
        </div>

        <div class="second-column col-12 md:col-6">
            <VideoPreview v-if="videoStore.videoURL"/>
        </div>
    </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import VideoPreview from '@/components/VideoPreview.vue'
import { useVideoStore } from '@/stores/video';

const options = ref([
    { name: 'Playlist' },
    { name: 'Video' },
])
const selectedOption = ref(options.value[0]);

const videoStore = useVideoStore()

const videoURLInput = computed({
  get() {
    return videoStore.videoURL
  },
  set(val) {
    videoStore.changeVideoURL(val)
  }
})
</script>

<style scoped>
.container {
    height: inherit;
    font-size: large;
}

.first-column {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    font-weight: bold;
    padding: 3%;
}

h1 {
    font-size: 70px;
    margin: 0;
}

.second-column {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
}
</style>
