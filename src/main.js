import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'


import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import VueEasyLightbox from 'vue-easy-lightbox'

import './assets/main.css'

const vuetify = createVuetify({
    components,
    directives,
    ssr: true,
})

const app = createApp(App)
app.use(createPinia())
app.use(router)
app.use(vuetify)
app.use(VueEasyLightbox)
app.mount('#app')

