import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

import posdata from "./modules/posdata"
import degreedata from "./modules/degreedata"
export default new Vuex.Store({
  modules: {
    posdata,
    degreedata,
  }
})
