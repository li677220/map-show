import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import ElementUI from "element-ui"
import 'element-ui/lib/theme-chalk/index.css';
import ECharts from "echarts"

Vue.use(ElementUI)
// Vue.use(axios) TypeError: Cannot read property 'protocol' of undefined
Vue.prototype.$axios = axios 
Vue.prototype.$echarts = ECharts
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

axios.defaults.baseURL = "http://47.114.43.156:80"
axios.defaults.timeout = 5000