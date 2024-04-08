
<template>
    <div class="card relative z-2">
        <Menubar>
            <template #start>
                <router-link to="/">
                    <img alt="logo" src="https://primefaces.org/cdn/primevue/images/logo.svg" height="40" class="mr-2" />
                </router-link>
            </template>
            <template #item="{ label, item, props, root, hasSubmenu }">
                Youtube
            </template>
            <template #end>

            </template>
        </Menubar>
        <!-- <ProgressBar mode="indeterminate" style="height: 6px"></ProgressBar> -->
    </div>
</template>
 
<script setup lang="ts">
</script>
 