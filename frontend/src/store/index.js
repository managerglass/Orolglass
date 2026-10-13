
import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: {
    //BASE_URL: 'https://orolglass.com.br/api/v1/',
    BASE_URL: 'http://127.0.0.1:8000/api/v1/',
    imagensDestques: [],
    imagensSobre: [],
    imagensObras: [],
    imagensEventos: [],
    destaques: []
  },

  getters: {},

  mutations: {},

  actions: {
    async getImages() {
      try {
        const response = await axios.get(`${this.state.BASE_URL}imagem?tipo=DESTAQUE`)
        return Array.isArray(response.data.results) ? response.data.results : []
      } catch (err) {
        console.error('Erro ao buscar imagens:', err)
        return []
      }
    },

    async getImagesAll() {
      try {
        const response = await axios.get(`${this.state.BASE_URL}imagem/`)
        return Array.isArray(response.data.results) ? response.data.results : []
      } catch (err) {
        console.error('Erro ao buscar todas as imagens:', err)
        return []
      }
    },

    async getAllDestaques() {
      try {
        const response = await axios.get(`${this.state.BASE_URL}destaques/`)
        return Array.isArray(response.data.results) ? response.data.results : []
      } catch (err) {
        console.error('Erro ao buscar destaques:', err)
        return []
      }
    },

    async getAllProjetos() {
      try {
        const response = await axios.get(`${this.state.BASE_URL}projeto`)
        return Array.isArray(response.data.results) ? response.data.results : []
      } catch (err) {
        console.error('Erro ao buscar projetos:', err)
        return []
      }
    },

    async getImagesFromProjetos() {
      try {
        const response = await axios.get(`${this.state.BASE_URL}imagem?tipo=PROJETO`)
        return response.data ?? []
      } catch (err) {
        console.error('Erro ao buscar imagens dos projetos:', err)
        return []
      }
    }
  },

  modules: {}
})
