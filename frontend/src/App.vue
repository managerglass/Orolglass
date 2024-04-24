<template>
  <navbar-component/>
  <router-view />
  <footer-component/>
</template>

<script>
import NavbarComponent from './components/NavBar/NavbarComponent.vue';
import FooterComponent from './components/Footer/FooterComponent.vue';

export default {
  name:'App',

  components: {
    NavbarComponent,
    FooterComponent
  },
  data() {
    return {

    }
  },


}
</script>
<style lang="scss"></style>
