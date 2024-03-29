<template>
     <p>@Copyright {{currentYear}}. Built for fun.</p>
</template>

<script setup lang="ts">
     import { computed } from 'vue';

     const currentYear = computed(() => {
          return new Date().getFullYear();
     });
</script>

<style scoped>

p{
     text-align: center;
     display: flex;
     flex-direction: column;
     justify-content: space-around;
}
</style>