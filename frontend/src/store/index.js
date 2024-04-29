import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: {
    BASE_URL: 'http://192.168.18.106:8000/api/v1/',
    imagensDestques: [],
    imagensSobre: [],
    imagensObras: [],
    imagensEventos: [],
    destaques: []
  },
  getters: {
  },
  mutations: {
  },
  actions: {
    async getImages({ commit }) {
      try {
        const response = await axios.get(`${this.state.BASE_URL}imagem?tipo=DESTAQUE`)
        return response.data
      } catch (err) {
        console.error(err)
      }
    },

    async getImagesAll({commit}) {
      try {
        const response = await axios.get(`${this.state.BASE_URL}imagem/`)
        return response.data
      } catch(err) {
        console.error(err);
      }
    },

    async getAllDestaques({ commit }) {
      try{
        const response = await axios.get(`${this.state.BASE_URL}destaques/`)
        return response.data
      }catch(err){
        console.error(err)
      }
    },

    async getAllProjetos({ commit }) {
      try {
        const response = await axios.get(`${this.state.BASE_URL}projeto`)
        console.log(response.data)
        return response.data
      } catch (err) {
        console.error(err)    
      }
    }
  },
  modules: {
  }
})
