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

  mounted() {
    this.getImagesall();
  },

  methods: {
    async getImagesall() {
      try {
        const response = await this.$store.dispatch('getImagesAll');

        const imagens = Array.isArray(response) ? response : [];

        this.$store.state.imagensDestques = imagens.filter(
          image => image.tipo?.tipo === "DESTAQUE"
        );

        this.$store.state.imagensSobre = imagens.filter(
          image => image.tipo?.tipo === "SOBRE"
        );

        this.$store.state.imagensObras = imagens.filter(
          image => image.tipo?.tipo === "PROJETO"
        );

        this.$store.state.imagensEventos = imagens.filter(
          image => image.tipo?.tipo === "EVENTO"
        );

      } catch (error) {
        console.error("Erro ao carregar imagens:", error);
      }
    }
  }
}
</script>

<style lang="scss"></style>