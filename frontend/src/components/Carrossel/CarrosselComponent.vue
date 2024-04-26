<template>
  <div class="relative min-h-[90vh] md:min-h-[100vh] overflow-x-hidden">
    <transition v-for="(image, index) in images" :key="index" name="slide">
      <div
        v-if="imagemAtual == index"
        class="carrossel bg-cover"
        :style="{ backgroundImage: 'url(' + image.imagem.arquivo + ')' }"
      >
        <div class="h-[90vh] md:h-[100vh] bg-black opacity-40"></div>
        <div class="absolute left-3 md:left-24 top-[60%] z-40 text-white">
          <h1 class="text-5xl">{{ image.titulo }}</h1>
          <p class="text-2xl">{{ image.descricao }}</p>
        </div>
      </div>
    </transition>
    <img
      v-if="imagemAtual + 1 < images.length"
      :src="images[imagemAtual + 1].imagem.arquivo"
      class="hidden"
    />
  </div>
</template>

<script>
export default {
  name: "CarrosselComponent",

  data() {
    return {
      images: [],
      imagemAtual: "",
    };
  },

  mounted() {
    let index = 0;

    setInterval(() => {
      this.imagemAtual = (this.imagemAtual + 1) % this.images.length;
      index = (index + 1) % this.images.length;
    }, 5000);

    this.getAllDestaques();
  },

  methods: {

    async getAllDestaques() {
      const response = await this.$store.dispatch("getAllDestaques");
      this.images = response;
    }
  }
};
</script>

<style>
.carrossel {
  @apply bg-cover absolute left-0 right-0 top-0 bottom-0  h-[90vh] md:h-[100vh];
}
.slide-enter-active,
.slide-leave-active {
  @apply transition-all duration-1000 ease-in-out;
}

.slide-enter-from {
  transform: translateX(-100%);
}
.slide-leave-to {
  transform: translateX(100%);
}
.hidden {
  opacity: 0;
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
</style>
