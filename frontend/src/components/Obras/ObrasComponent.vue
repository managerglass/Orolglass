<template>
  <div class="py-44 px-6">
    <div class="container-titulo">
      <h1 class="text-azul_logo text-2xl md:text-4xl">
        OBRAS <span class="text-laranja_logo">E PRODUTOS</span>
      </h1>
    </div>
    <div class="container-carrossel-projetos">
      <div class="w-full overflow-x-scroll h-96 flex gap-4 px-6 py-8">
        <div
          v-for="projeto in projetos"
          :key="projeto.id"
          @mouseenter="onMouseEnter(projeto)"
          @mouseleave="onMouseLeave(projeto)"
        >
          <div
            class="w-72 h-60 transition transform hover:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:transform-none ..."
            :style="{
              background: `url(${projeto.imagem[0].arquivo})`,
              backgroundSize: 'cover',
              backgroundPosition: 'center',
            }"
          ></div>
          <p class="text-black">{{ projeto.titulo }}</p>
        </div>
      </div>
    </div>
    <div>
      <p>imagens projetos</p>
    </div>
  </div>
</template>

<script>
import CarrosselSample from '../Carrossel/CarrosselSample.vue'

export default {

  name: "ObrasComponent",

  components: {
    CarrosselSample
  },

  data() {
    return {
      images: [],
      projetos: [],
      hoveringItem: null,
    };
  },

  mounted() {
    this.getAllProjetos();
  },

  methods: {
    async getAllProjetos() {
      this.projetos = await this.$store.dispatch("getAllProjetos");
    },

    onMouseEnter(item) {
      this.hoveringItem = item;
    },
    onMouseLeave() {
      this.hoveringItem = null;
    },
    isHovering(item) {
      return this.hoveringItem === item;
    },
  },
};
</script>

<style scoped lan="scss">
.container-titulo {
  @apply w-full flex justify-center font-bold;
}
.container-carrossel-projetos {
  @apply w-full text-white flex justify-center;
}
</style>