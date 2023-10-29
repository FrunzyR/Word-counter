<script setup lang="ts">
import { RouterView } from 'vue-router'
import Navbar from '@/components/Navbar.vue'
import CustomFooter from './components/CustomFooter.vue';
</script>

<template>
    <header>
        <Navbar />
    </header>

    <main>
        <Suspense>
            <RouterView />
        </Suspense>

    </main>

    <footer>
        <CustomFooter />
    </footer>
</template>

<style scoped>
header {
    height: 10vh;
}

main {
    max-width: 1000px;
    margin: 0 auto;
    /* height: 70vh; */
}

footer {
    height: 14vh;
}
</style>
