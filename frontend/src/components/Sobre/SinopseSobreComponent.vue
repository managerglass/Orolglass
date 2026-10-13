
<template>
  <div class="px-4 py-12 flex flex-col gap-6 md:gap-12 w-full">

    <h1 class="title-section text-center">
      Sobre <span>Orolglass</span>
    </h1>

    <div class="flex flex-col md:flex-row justify-between px-4 md:px-20 items-start gap-8">

      <div class="w-full md:w-[50%] flex flex-col gap-6">

        <template v-if="sinopse">
          <p class="text-xl text-justify">
            {{ sinopse.sobre }}
          </p>

          <p class="text-xl text-justify hidden md:block">
            {{ sinopse.origem }}
          </p>

          <router-link
            class="px-4 py-1 bg-cor_fundo w-full md:w-44 text-center text-white font-bold hover:bg-azul_logo duration-300"
            to="/sobre"
          >
            Ver mais
          </router-link>
        </template>

        <p v-else class="text-xl text-gray-500">
          Em breve, conheça mais sobre a Orolglass.
        </p>

      </div>

      <img
        v-if="imagem"
        class="w-full md:w-[40%]"
        :src="imagem"
        alt="Conheça a Orolglass"
      />

    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'SinopseSobreComponent',

  data() {
    return {
      sinopse: null,
      imagem: ''
    }
  },

  mounted() {
    this.getSobreSinopse()
  },

  methods: {
    async getSobreSinopse() {
      try {
        const response = await axios.get(
          `${this.$store.state.BASE_URL}sobre/`
        )

        const resultados = response.data.results || []

        if (resultados.length > 0) {
          this.sinopse = resultados[0]
          this.imagem = this.sinopse.imagens?.[0]?.arquivo || ''
        }

      } catch (err) {
        console.error('Erro ao carregar informações da empresa:', err)
      }
    }
  }
}
</script>

<style scoped lang="scss"></style>
