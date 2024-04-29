[<template>
  <div>
    <div
      v-for="(imagem, index) in imagens"
      :key="index"
      class="bg-cover w-72 h-60 absolute right-0 left-0 bottom-0 top-0"
      :style="{ backgroundImage: 'url(' + imagem.arquivo + ')' }"
    >
    </div>
  </div>
</template>

<script>
export default {
  name: "CarrosselSample",

  data() {
    return {
      imagemAtual: "",
    };
  },

  props: {
    imagens: {
      type: Array,
      required: true,
    },
  },

  mounted() {
    let index = 0;

    setInterval(() => {
      this.imagemAtual = (this.imagemAtual + 1) % this.imagens.length;
      index = (index + 1) % this.imagens.length;
    }, 1000);
  },
};
</script>

<style scoped lang="scss">
</style>]