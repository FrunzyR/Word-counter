import {createRouter, createWebHistory} from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import WordAnalysisView from '@/views/WordAnalysisView.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomeView
        },
        {

            path: '/analysis',
            name: 'analysis',
            component: WordAnalysisView
        },
    ]
})

export default router
