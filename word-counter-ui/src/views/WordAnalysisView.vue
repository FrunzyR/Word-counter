<template>
    <Toast/>
    <div v-if="!responseData" class="w-full flex justify-content-center">
        <ProgressSpinner/>
    </div>
    <div v-else class="container grid">
        <div class="first-column col-12 md:col-6">
            <h1>{{ responseData.videoTitle }}</h1>
            <VideoPreview />
        </div>

        <div class="second-column col-12 md:col-6">
            <DataTable :value="responseData.results">
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
import { ref } from 'vue';
import { useToast } from 'primevue/usetoast';

const toast = useToast();
const videoStore = useVideoStore()

const apiUrl = "/api/analyse?" + new URLSearchParams({
    videoId: videoStore.videoId,
    lang: "en"
});
const isLoading = ref(true);
const error = ref(null);
const responseData = ref<any>(null);

const show = () => {
    toast.add({ severity: 'error', summary: 'Error', detail: 'Something went wrong', life: 10000 });
};

const fetchData = async () => {
  try {
    const response = await fetch(apiUrl);
    if (!response.ok) {
      throw new Error();
    }
    responseData.value = await response.json();
  } catch {
    show()
  } finally {
    isLoading.value = false;
  }
};

fetchData();
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
