<template>
  <SobreComponent :details_sobre="sobre" :sobre_valores="sobreValores" :sobre_crencas="sobreCrencas"/>  

  <ServicosComponent />
</template>

<script>
import axios from 'axios'
import SobreComponent from '../components/Sobre/SobreComponent.vue'
import ServicosComponent from '@/components/Servicos/ServicosComponent.vue'

export default {

  name: 'SobreView',
  components: {
    SobreComponent,
    ServicosComponent
  },
  data() {
    return {
      sobre: {},
      sobreValores: {},
      sobreCrencas: {}
    }
  },

  created() {
    this.getAbout();
    this.getValues();
    this.getCrencas();
  },

  methods: {
    async getAbout() {
      try {
        const response = await axios.get(`${this.$store.state.BASE_URL}sobre`)
        this.sobre = response.data
      } catch(err) {
        console.error(err);
      }
    },
    async getValues() {
      try {
        const response = await axios.get(`${this.$store.state.BASE_URL}valores`)
        this.sobreValores = response.data
      } catch(err) {
        console.error(err);
      }
    },
    async getCrencas() {
      try {
        const response = await axios.get(`${this.$store.state.BASE_URL}crencas`)
        this.sobreCrencas = response.data
      } catch(err) {
        console.error(err);
      }
    },
  }
}

</script>

<style lang="scss">

</style>