<template>
  <div>
    <div class="bg-cover absolute left-0 right-0 top-0 -z-10 bottom-0 h-[30vh] md:h-[30vh]" :style="{
      backgroundImage:
        'url(http://orolglass.com.br:9000/media/imagens/8.jpg)',
    }"></div>
    <div class="bg-cover bg-black/40 h-[30vh]"></div>
    <div class="container-sobre">
      <h1 class="bg-white text-center">
        SOBRE <span class="text-laranja_logo">OROLGLASS</span>
      </h1>
      <div class="container-main-sobre mt-8">
        <div class="contaier-esquerda">
          <h2 class="text-xl text-cor_texto font-bold pb-4">
            Nasceu para ser a diferença
          </h2>
          <p>{{ details_sobre.sobre }}</p>

          <h2 class="text-xl text-cor_texto font-bold pb-4 py-6">
            Em busca da origem
          </h2>
          <p>{{ details_sobre.origem }}</p>

          <h2 class="text-xl text-cor_texto font-bold pb-4 py-6">
            Lema e crença norteadora
          </h2>
          <p>{{ details_sobre.lema }}</p>

          <h2 class="text-xl text-cor_texto font-bold pb-4 py-6">Missão</h2>
          <p>{{ details_sobre.missao }}</p>

          <h2 class="text-xl text-cor_texto font-bold pb-4 py-6">Visão</h2>
          <p>{{ details_sobre.visao }}</p>

          <div class="flex flex-col gap-6 my-6">
            <div class="bg-slate-50 p-6 flex flex-col gap-6">
              <h3 class="text-xl text-cor_texto font-bold">Crenças</h3>
              <div class="flex flex-col gap-2">
                <p v-for="crenca in sobre_crencas" :key="crenca.id">
                  - {{ crenca.crenca }}
                </p>
              </div>
            </div>

            <div class="bg-slate-50 p-6 flex flex-col gap-6">
              <h3 class="text-xl text-cor_texto font-bold">Valores</h3>
              <div class="flex flex-col gap-2">
                <p v-for="valor in sobre_valores" :key="valor.id">
                  - {{ valor.valor }}
                </p>
              </div>
            </div>
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
      <div class="flex flex-col gap-10 p-4 md:w-[50vw] mx-auto">
        <h1 class="text-2xl text-azul_logo text-center font-bold">Enviar <span class="text-laranja_logo">Mensagem</span>
        </h1>
        <form class="flex flex-col gap-8">
          <div class="relative w-full">
            <input id="nome"
              class="py-2 outline-none border-b-2 focus:border-laranja_logo relative z-10 bg-transparent w-full"
              type="text" placeholder=" " v-model="nome" @focus="isFocused = true" @blur="isFocused = false" />
            <label class="absolute left-0 transition-all duration-300"
              :class="{ 'text-azul_logo text-xs': isFocused || nome }"
              :style="{ top: isFocused || nome ? '-10px' : '2px' }">
              Nome Completo
            </label>
          </div>


          <div class="relative w-full">
            <input id="nome"
              class="py-2 outline-none border-b-2 focus:border-laranja_logo relative z-10 bg-transparent w-full"
              type="text" placeholder=" " v-model="email" @focus="isFocusedEmail = true"
              @blur="isFocusedEmail = false" />
            <label class="absolute left-0 transition-all duration-300"
              :class="{ 'text-azul_logo text-xs': isFocusedEmail || email }"
              :style="{ top: isFocusedEmail || email ? '-10px' : '2px' }">
              E-mail
            </label>
          </div>

          <div class="relative w-full">
            <select id="numero"
              class="py-2 outline-none border-b-2 focus:border-laranja_logo relative z-10 bg-transparent w-full"
              @focus="isFocusedNumero = true" @blur="isFocusedNumero = false" v-model="numero">
              <option value="" disabled selected hidden></option>
              <!-- Adicione opções conforme necessário -->
              <option value="55032999362017">Comercial</option>
              <option value="55032998502027">Vendas</option>
              <option value="55032988607060">Fábrica</option>
              <option value="55032998061820">Técnico</option>
              <option value="55032984923475">Manutenção</option>
            </select>
            <label class="absolute left-0 top-2 transition-all duration-300 pointer-events-none"
              :class="{ 'text-azul_logo text-xs': isFocusedNumero || numero }"
              :style="{ top: isFocusedNumero || numero ? '-10px' : '2px' }">
              Falar com
            </label>
          </div>

          <div class="relative w-full">
            <textarea
              class="py-2 px-2 outline-none border-2 focus:border-laranja_logo relative z-10 bg-transparent w-full"
              placeholder="Avaliação" rows="5" maxlength="500" v-model="assunto"></textarea>
          </div>

          <div class="w-full">
            <button @click="pushMessage"
              class="text-center font-bold bg-cor_fundo text-white py-2 w-full">Enviar</button>
          </div>

        </form>
      </div>
    </div>
  </div>
</template>

<script>
import EnderecoComponent from "./EnderecoComponent.vue";
import axios from "axios";

export default {
  name: "SobreComponent",

  components: {
    EnderecoComponent,
  },
  data() {
    return {
      enderecos: [],
      isFocused: false,
      isFocusedEmail: false,
      isFocusedNumero: false,
      email: '',
      nome: '',
      assunto: '',
      numero: ''
    };
  },

  props: {
    details_sobre: {
      type: Object,
      required: true,
    },
    sobre_valores: {
      type: Object,
      required: true,
    },
    sobre_crencas: {
      type: Object,
      required: true,
    },
  },

  mounted() {
    this.getEnderecos();
  },

  methods: {
    async getEnderecos() {
      const response = await axios.get(
        `${this.$store.state.BASE_URL}enderecos/`
      );
      this.enderecos = response.data.results
    },
    async pushMessage() {
      try {
        const url = `https://api.whatsapp.com/send?phone=${this.numero}&text=Nome:%20${this.nome}%0AE-mail:%20${this.email}%0A%0AAssunto:%0A${this.assunto}`
        window.open(url, '_blank')
      } catch (err) {
        console.error(err);
      }
    }
  },
};
</script>

<style lang="scss">
.container-sobre {
  @apply px-6 py-10;
}

.container-sobre h1 {
  @apply md:text-4xl text-2xl text-azul_logo font-bold
}

.container-main-sobre {
  @apply flex flex-col md:flex-row w-full;
}

.contaier-esquerda {
  @apply w-full;
}

.contaier-direita {
  @apply w-full;
}
</style>
