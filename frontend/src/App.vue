<template>
  <navbar-component />
  <router-view />
  <footer-component />
</template>

<script>
import NavbarComponent from './components/NavBar/NavbarComponent.vue';
import FooterComponent from './components/Footer/FooterComponent.vue';

export default {
  name: 'App',

  components: {
    NavbarComponent,
    FooterComponent
  },
  data() {
    return {

    }
  },

  mounted() {
    this.getImagesall()
  },

  methods: {
    async getImagesall() {
      const response = await this.$store.dispatch('getImagesAll');
      this.$store.state.imagensDestques = response.filter(image => image.tipo.tipo === "DESTAQUE");
      this.$store.state.imagensSobre = response.filter(image => image.tipo.tipo === "SOBRE")
      this.$store.state.imagensObras = response.filter(image => image.tipo.tipo === "PROJETO")
      this.$store.state.imagensEventos = response.filter(image => image.tipo.tipo === "EVENTO")
    }
  }


}
</script>
<style lang="scss"></style>
