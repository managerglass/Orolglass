<template>
  <div>
    <div>
      <h1><span>OBRAS</span> E PRODUTOS</h1>
    </div>
    <div>
      <p>lista de tipos</p>
    </div>
    <div>
      <p>imagens projetos</p>
    </div>
  </div>
</template>

<script>
export default {

  name: "ObrasComponent",

  components: {},

  data() {
    return {
      images: [],
      projetos: []
    };
  },

  mounted() {
    this.getImagesObras()
    this.getAllProjetos()
  },

  methods: {
    getImagesObras() {
      this.images = this.$store.state.imagensObras;
    },

    async getAllProjetos() {
        this.projetos = await this.$store.dispatch('getAllProjetos')
    }
  },
};
</script>

<style scoped lan="scss">

</style>