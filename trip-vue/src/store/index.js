import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    username:'',
    home_data:{},
  },
  mutations: {
    getusername(state,username) {
      this.state.username = username
    },
    gethomedata(state,homedata) {
      console.log(homedata);
      this.state.home_data = homedata
    }
  },
  actions: {
  },
  modules: {
  }
})
