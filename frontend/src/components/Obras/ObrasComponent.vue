<template>
  <div>
    <div
      class="bg-cover absolute left-0 right-0 top-0 -z-10 bottom-0 h-[30vh] md:h-[30vh]"
      :style="{
        backgroundImage:
          'url(http://192.168.18.106:8000/media/imagens/3_8qdtQcf_ocLULKX.jpg)',
      }"
    ></div>
    <div
      class="h-[30vh]"
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
        <div class="w-full overflow-x-auto h-[42vh] md:h-[50vh] flex gap-4 px-6">
          <div
            v-for="projeto in projetos"
            :key="projeto.id"
            @mouseenter="onMouseEnter(projeto)"
            @mouseleave="onMouseLeave(projeto)"
            class="bg-slate-50 h-[39vh] md:h-[47vh] p-5"
            @click.prevent="activeModal1(projeto.imagem)"
          >
            <div
              class="mb-2 w-72 h-60 md: h-30 transition transform hover:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:transform-none ..."
              :style="{
                background: `url(${projeto.imagem[0].arquivo})`,
                backgroundSize: 'cover',
                backgroundPosition: 'center',
              }"
            ></div>
            <p class="text-xl text-laranja_logo font-bold">
              {{ projeto.titulo }}
            </p>
            <p
              class="text-cor_texto overflow-hidden text-ellipsis whitespace-nowrap max-w-72"
            >
              {{ projeto.descricao }}
            </p>
          </div>
        </div>
        <modal-projeto
          :imagens="projetoImagem"
          :isModal="isOpen1"
          @fechar="activeModal1"
        />
      </div>
    </div>
    <div class="w-full flex justify-center text-center mt-5">
      <h1
        class="text-azul_logo tracking-widest text-2xl font-bold md:text-4xl w-64 md:w-96 mb-3 md:mb-6"
      >
        GALERIA
      </h1>
    </div>
    <div class="flex flex-wrap justify-center gap-5">
      <div
        v-for="(imagem, index) in todasImagens"
        :key="imagem.id"
        class="mt-1 mb-1"
      >
        <img
          :src="imagem.arquivo"
          alt="imagem projeto"
          class="w-80 h-60 md:w-[30vw] md:h-[40vh]"
          @click.prevent="this.activeModal2(index)"
        />
        <modal-visualizar-imagens
          v-if="isOpen2 == true && index === indexAtual"
          @fechar="activeModal2"
          :imagens="imagem"
          @passarImagem="passarImagem"
          @voltarImagem="voltarImagem"
        />
      </div>
    </div>
    <div class="flex justify-center">
      <button
        v-if="!this.finalPagina"
        class="text-center font-bold bg-cor_fundo text-white py-2 w-52 mb-6 md:w-[13vw]"
        @click.prevent="setProximasImagens"
      >
        Carregar mais...
      </button>
    </div>
  </div>
</template>

<script>
import CarrosselSample from "../Carrossel/CarrosselSample.vue";
import ModalVisualizarImagens from "./ModalVisualizarImagens.vue";
import ModalProjeto from "./ModalProjeto.vue";
import axios from "axios";

export default {
  name: "ObrasComponent",

  components: {
    CarrosselSample,
    ModalVisualizarImagens,
    ModalProjeto,
  },

  data() {
    return {
      projetos: [],
      imagensProjeto: [],
      todasImagens: [],
      hoveringItem: null,
      isOpen1: false,
      isOpen2: false,
      totalImagens: "",
      proximaUrl: "",
      finalPagina: false,
      indexAtual: 0,
      projetoImagem: [],
    };
  },

  mounted() {
    this.getAllProjetos();
    this.setAllImagens();
  },

  methods: {
    async getAllProjetos() {
      this.projetos = await this.$store.dispatch("getAllProjetos");
    },

    async setAllImagens() {
      const obetoImagens = await this.$store.dispatch("getImagesFromProjetos");
      this.todasImagens = obetoImagens.results;
      this.proximaUrl = obetoImagens.next;
      this.totalImagens = obetoImagens.count;
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

    activeModal1(imagens) {
      this.projetoImagem = imagens;
      this.isOpen1 = !this.isOpen1;
    },

    activeModal2(index) {
      this.indexAtual = index;
      this.isOpen2 = !this.isOpen2;
    },

    async setProximasImagens() {
      try {
        const response = await axios.get(`${this.proximaUrl}`);
        if (this.todasImagens.length != response.data.count - 1) {
          this.proximaUrl = response.data.next;
          this.todasImagens.push(...response.data.results);
        } else {
          this.finalPagina = true;
        }
      } catch (err) {
        console.error(err);
      }
    },

    passarImagem() {
      this.indexAtual < this.todasImagens.length - 1
        ? this.indexAtual++
        : (this.indexAtual = this.indexAtual = 0);
    },

    voltarImagem() {
      this.indexAtual > 0
        ? this.indexAtual--
        : (this.indexAtual = this.todasImagens.length - 1);
    },
  },
};
</script>

<style scoped lan="scss">
.container-titulo {
  @apply w-full flex justify-center font-bold pt-10;
}
.container-carrossel-projetos {
  @apply w-full text-white flex justify-center;
}
</style>