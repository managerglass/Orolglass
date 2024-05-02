<template>
  <div class="container-section">
    <h1 class="title-section">Algumas <span>Obras</span></h1>
    <div class="w-full overflow-x-scroll h-96 flex gap-6 px-6 py-8">
      <div v-for="(imagem, index) in imagens" :key="imagem.id" class="relative">
        <div
          class="w-72 h-60"
          :style="{
            background: `url(${imagem.arquivo})`,
            backgroundSize: 'cover',
            backgroundPosition: 'center',
          }"
          @click.prevent="activeModal(index)"
        ></div>
        <p>{{ imagem.titulo }}</p>
        <modal-visualizar-imagens
          v-if="isOpen == true && index === indexAtual"
          :imagens="imagem"
          @fechar="activeModal"
          @passarImagem="passarImagem"
          @voltarImagem="voltarImagem"
        />
      </div>
    </div>
  </div>
</template>

<script>
import ModalVisualizarImagens from "./ModalVisualizarImagens.vue";

export default {
  name: "PreviewObrasComponent",

  components: {
    ModalVisualizarImagens,
  },

  data() {
    return {
      imagens: [],
      indexAtual: 0,
      isOpen: false
    };
  },

  mounted() {
    this.getImagensDestaque();
  },

  methods: {
    async getImagensDestaque() {
      this.imagens = await this.$store.dispatch('getImages')
    },

    activeModal(index) {
      this.indexAtual = index;
      this.isOpen = !this.isOpen;
    },

    passarImagem() {
      this.indexAtual < this.imagens.length - 1
        ? this.indexAtual++
        : (this.indexAtual = this.indexAtual = 0);
    },

    voltarImagem() {
      this.indexAtual > 0
        ? this.indexAtual--
        : (this.indexAtual = this.imagens.length - 1);
    },
  },
};
</script>

<style scoped lang="scss"></style>