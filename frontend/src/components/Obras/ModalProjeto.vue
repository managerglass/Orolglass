<template>
  <div>
    <div v-for="(imagem, index) in imagens" :key="imagem.id">
      <modal-visualizar-imagens
        v-if="isModalFunction == true && index === indexAtual"
        @fechar="fechar"
        :imagens="imagem"
        @passarImagem="passarImagem"
        @voltarImagem="voltarImagem"
      />
    </div>
  </div>
</template>

<script>
import ModalVisualizarImagens from "./ModalVisualizarImagens.vue";

export default {
  name: "ModalProjeto",

  components: {
    ModalVisualizarImagens,
  },

  props: {
    imagens: {
      type: Array,
    },

    isModal: Boolean
  },

  data() {
    return {
      indexAtual: 0,
      
    };
  },

  computed: {
    isModalFunction() {
        console.log(this.isModal)
        return this.isModal
    }
  },

  methods: {

    passarImagem() {
      this.indexAtual < this.imagens.length - 1
        ? this.indexAtual++
        : (this.indexAtual = this.indexAtual = 0);
      console.log(this.indexAtual);
    },

    voltarImagem() {
      this.indexAtual > 0
        ? this.indexAtual--
        : (this.indexAtual = this.imagens.length - 1);
      console.log(this.indexAtual);
    },

    fechar() {
        this.$emit("fechar")
    }
  },
};
</script>

<style scoped lang="scss">
</style>