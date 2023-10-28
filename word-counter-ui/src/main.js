import { createApp } from 'vue'
import App from './App.vue'
import PrimeVue from 'primevue/config';
import 'primeflex/primeflex.css'

let app = createApp(App);
app.use(PrimeVue)
app.mount('#app')
