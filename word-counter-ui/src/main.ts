import './assets/main.css'

import {createApp} from 'vue'
import {createPinia} from 'pinia'
import PrimeVue from 'primevue/config';
import 'primeflex/primeflex.scss';
import 'primevue/resources/themes/lara-light-indigo/theme.css'
import 'primevue/resources/primevue.min.css'

import Dropdown from 'primevue/dropdown';


import App from './App.vue'
import router from './router'
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';
import Menubar from 'primevue/menubar';

const app = createApp(App)

app.use(createPinia())
app.use(PrimeVue)
app.use(router)

app.component('Dropdown', Dropdown);
app.component('InputText', InputText)
app.component('Button', Button)
app.component('Menubar', Menubar)

app.mount('#app')
