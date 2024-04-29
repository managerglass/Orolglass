<template>
  <div>
    <div
      class="bg-cover absolute left-0 right-0 top-0 -z-10 bottom-0 h-[30vh] md:h-[30vh]"
      :style="{
        backgroundImage:
          'url(http://192.168.18.88:8000/media/imagens/3_8qdtQcf_ocLULKX.jpg)',
      }"
    ></div>
    <div
      class="bg-cover bg-black/20 absolute left-0 right-0 top-0 -z-10 bottom-0 h-[30vh] md:h-[30vh]"
    ></div>
    <div>
      <div class="container-titulo">
        <h1
          class="text-azul_logo text-2xl md:text-4xl w-64 md:w-96 bg-white text-center"
        >
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
            @click.prevent="activeModal"
          >
            <div
              class="w-72 h-60 transition transform hover:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:transform-none ..."
              :style="{
                background: `url(${projeto.imagem[0].arquivo})`,
                backgroundSize: 'cover',
                backgroundPosition: 'center',
              }"
            ></div>
            <modal-visualizar-imagens
              v-if="isOpen == true"
              @fechar="activeModal"
              :imagens="projeto.imagem"
            />
            <p class="text-black">{{ projeto.titulo }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import CarrosselSample from "../Carrossel/CarrosselSample.vue";
import ModalVisualizarImagens from "./ModalVisualizarImagens.vue";

export default {
  name: "ObrasComponent",

  components: {
    CarrosselSample,
    ModalVisualizarImagens,
  },

  data() {
    return {
      images: [],
      projetos: [],
      hoveringItem: null,
      isOpen: false,
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

    activeModal() {
      this.isOpen = !this.isOpen;
    },
  },
};
</script>

<style scoped lan="scss">
.container-titulo {
  @apply w-full flex justify-center font-bold mt-56;
}
.container-carrossel-projetos {
  @apply w-full text-white flex justify-center;
}
</style>