<template>
  <div
    id="controls-carousel"
    class="fixed right-0 left-0 bottom-0 top-0 z-50 w-full bg-black/50"
    data-carousel="static"
  >
    <div class="relative h-56 overflow-hidden rounded-lg md:h-96">
      <div class="h-50" data-carousel-item>
        <img
          :src="imagens.arquivo"
          class="fixed md:h-[80vh] -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2"
          alt="..."
        />
      </div>
    </div>
    <button
      type="button"
      class="absolute bottom-72 end-5 z-30 flex items-center justify-center h-full px-4 cursor-pointer group focus:outline-none"
      @click.stop="fechar"
    >
      <span
        class="inline-flex items-center justify-center w-10 h-10 rounded-full bg-white/30 dark:bg-gray-800/30 group-hover:bg-white/50 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none"
      >
        <i class="fa-solid fa-xmark"></i>
        <span class="sr-only">Previous</span>
      </span>
    </button>
    <button
      type="button"
      class="absolute top-0 start-28 z-30 flex items-center justify-center h-full px-4 cursor-pointer group focus:outline-none"
      data-carousel-prev
      @click.stop="voltarImagem"
    >
      <span
        class="inline-flex items-center justify-center w-10 h-10 rounded-full bg-white/30 dark:bg-gray-800/30 group-hover:bg-white/50 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none"
      >
        <svg
          class="w-4 h-4 text-white rtl:rotate-180"
          aria-hidden="true"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 6 10"
        >
          <path
            stroke="currentColor"
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M5 1 1 5l4 4"
          />
        </svg>
        <span class="sr-only">Previous</span>
      </span>
    </button>
    <button
      type="button"
      class="absolute top-0 end-28 z-30 flex items-center justify-center h-full px-4 cursor-pointer group focus:outline-none"
      data-carousel-next
      @click.stop="passarImagem"
    >
      <span
        class="inline-flex items-center justify-center w-10 h-10 rounded-full bg-white/30 dark:bg-gray-800/30 group-hover:bg-white/50 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none"
      >
        <svg
          class="w-4 h-4 text-white rtl:rotate-180"
          aria-hidden="true"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 6 10"
        >
          <path
            stroke="currentColor"
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="m1 9 4-4-4-4"
          />
        </svg>
        <span class="sr-only">Next</span>
      </span>
    </button>
  </div>
</template>

<script>
export default {
  name: "ModalVisualizarImagens",

  props: {
    imagens: {
      type: Object,
      required: true,
    },

    imagemIndex: {
      type: Number,
      required: true,
    },
  },

  data() {
    return {
      imagemAtual: 0,
    };
  },

  mounted() {
    this.imagemAtual = this.imagemIndex;
  },

  methods: {
    passarImagem() {
      this.$emit("passarImagem");
    },

    voltarImagem() {
      this.$emit("voltarImagem");
    },

    fechar() {
      this.$emit("fechar")
    }
  },
};
</script>

<style  scoped lang="scss">
</style>