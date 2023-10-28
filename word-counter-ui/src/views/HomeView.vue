<template>
    <div class="container">
        <div class="first-column">
            <h1>Youtube caption word counter</h1>
            <div class="flex flex-column gap-2">
                <label for="selectedOption">Select content type</label>
                <Dropdown id="selectedOption" v-model="selectedOption" :options="options" optionLabel="name" class="w-full" />
            </div>
            <div class="flex flex-column gap-2">
                <label for="url">Paste the link of a {{ selectedOption.name }}</label>
                <InputText id="url" placeholder="Your URL"/>
            </div>
            <Button label="Count"  />
        </div>

        <div class="second-column">

        </div>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const options = ref([
    { name: 'Playlist' },
    { name: 'Video' },
])
const selectedOption = ref(options.value[0]);
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
    justify-content: space-around;
    font-weight: bold;
    padding: 2%;
}

h1 {
    font-size: 80px;
    margin: 0;
}

.second-column {
    background-color: aqua;
    width: 50%;
}
</style>
