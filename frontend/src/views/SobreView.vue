<template>
  <SobreComponent :details_sobre="sobre" :sobre_valores="sobreValores" :sobre_crencas="sobreCrencas"/>  

</template>

<script>
import axios from 'axios'
import SobreComponent from '../components/Sobre/SobreComponent.vue'

export default {

  name: 'SobreView',
  components: {
    SobreComponent,
  },
  data() {
    return {
      sobre: {},
      sobreValores: {},
      sobreCrencas: {}
    }
  },

  mounted() {
    this.getAbout();
    this.getValues();
    this.getCrencas();
  },

  methods: {
    async getAbout() {
      try {
        const response = await axios.get(`${this.$store.state.BASE_URL}sobre/`)
        this.sobre = response.data.results[0]
      } catch(err) {
        console.error(err);
      }
    },
    async getValues() {
      try {
        const response = await axios.get(`${this.$store.state.BASE_URL}valores`)
        this.sobreValores = response.data.results
      } catch(err) {
        console.error(err);
      }
    },
    async getCrencas() {
      try {
        const response = await axios.get(`${this.$store.state.BASE_URL}crencas`)
        this.sobreCrencas = response.data.results
      } catch(err) {
        console.error(err);
      }
    },
  }
}

</script>

<style lang="scss">

</style>