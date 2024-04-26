<template>
  <div class="container-sobre">
    <h1>SOBRE A <span class="text-laranja_logo">OROLGLASS</span></h1>
    <div class="container-main-sobre">
      <div class="contaier-esquerda">
        <h2 class="text-xl text-cor_texto font-bold pb-4">Nasceu para ser a diferença</h2>
        <p>{{ details_sobre.sobre }}</p>

        <h2 class="text-xl text-cor_texto font-bold pb-4 py-6">Em busca da origem</h2>
        <p>{{ details_sobre.origem }}</p>

        <h2 class="text-xl text-cor_texto font-bold pb-4 py-6">Lema e crença norteadora</h2>
        <p>{{ details_sobre.lema }}</p>

        <h2 class="text-xl text-cor_texto font-bold pb-4 py-6">Missão</h2>
        <p>{{ details_sobre.missao }}</p>

        <h2 class="text-xl text-cor_texto font-bold pb-4 py-6">Visão</h2>
        <p>{{ details_sobre.visao }}</p>

        <div>
          <h3 class="text-xl text-cor_texto font-bold pb-4 py-6">Crenças</h3>
          <p v-for="crenca in sobre_crencas" :key="crenca.id">{{ crenca.crenca }}</p>
        </div>

        <div>
          <h3 class="text-xl text-cor_texto font-bold pb-4 py-6">Valores</h3>
          <p v-for="valor in sobre_valores" :key="valor.id">{{ valor.valor }}</p>
        </div>
      </div>

      <div class="contaier-direita">
        <div v-for="imagen in details_sobre.imagens" :key="imagen.id">
          <img :src="imagen.arquivo" />
        </div>
      </div>
    </div>

    <div class="container-enderecos">
      <div class="container-section">
        <h1 class="title-section">Onde <span>Estamos?</span></h1>
        <div v-for="endereco in enderecos" :key="endereco.id">
          <div>
            <EnderecoComponent :endereco="endereco" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import EnderecoComponent from './EnderecoComponent.vue';
import axios from 'axios';

export default {
  name: 'SobreComponent',

  components: {
    EnderecoComponent
  },
  data() {
    return {
      enderecos: [],
    }
  },

  props: {
    details_sobre: {
      type: Object,
      required: true
    },
    sobre_valores: {
      type: Object,
      required: true
    },
    sobre_crencas: {
      type: Object,
      required: true
    }
  },

  mounted() {
    this.getEnderecos()
  },

  methods: {
    async getEnderecos() {
      const response = await axios.get(`${this.$store.state.BASE_URL}enderecos/`)
      this.enderecos = response.data;
    }
  }

}
</script>

<style lang="scss">
.container-sobre {
  @apply px-6 py-44
}

.container-sobre h1 {
  @apply text-4xl text-azul_logo font-bold py-3
}

.container-main-sobre {
  @apply flex flex-col md:flex-row w-full
}

.contaier-esquerda {
  @apply w-full
}

.contaier-direita {
  @apply w-full
}
</style>
