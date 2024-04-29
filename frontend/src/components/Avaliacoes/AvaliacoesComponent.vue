<template>

    <div>
        <h1 class="title-section">Avaliações</h1>

        <div class="flex gap-6 mx-4 overflow-x-scroll py-12">
            <div v-for="avaliacao in avaliacoes" :key="avaliacao.id"
                class="bg-slate-50 p-4 py-12 flex flex-col text-center ">
                <div class="w-52">
                    <i v-if="avaliacao.rede_social === 'WHATSAPP'" class="fab fa-whatsapp text-5xl text-cor_texto"></i>
                    <i v-else-if="avaliacao.rede_social === 'INSTAGRAM'"
                        class="fab fa-instagram text-5xl text-cor_texto"></i>
                    <i v-else-if="avaliacao.rede_social === 'FACEBOOK'"
                        class="fab fa-facebook text-5xl text-cor_texto"></i>
                    <p class="text-xl py-6"><span class="font-bold">Nome:</span> {{ avaliacao.nome }}</p>
                    <p class="text-justify">{{ avaliacao.relato }}</p>
                </div>
            </div>
        </div>
        <!-- BOTÃO ADICIONAR AVALIAÇÃO -->
        <div class="w-full px-4 py-2">
            <button @click.prevent="activeModal" class="w-full bg-cor_fundo text-white font-bold py-2 ">Adicionar
                avaliação</button>
        </div>
        <NovaAvaliacao v-if="isOpen == true" @fechar="activeModal" @atualizar="getAvaliacoes"/>
    </div>


</template>

<script>
import axios from 'axios';
import NovaAvaliacao from './NovaAvaliacao.vue'

export default {
    name: 'AvalicacoesComponent',
    components: {
        NovaAvaliacao
    },

    data() {
        return {
            avaliacoes: [],
            isOpen: false,
        }
    },

    mounted() {
        this.getAvaliacoes()
    },

    methods: {
        activeModal() {
            this.isOpen = !this.isOpen;
        },

        async getAvaliacoes() {
            try {
                const response = await axios.get(`${this.$store.state.BASE_URL}avaliacoes/`)
                console.log(response.data);
                this.avaliacoes = response.data

            } catch (err) {
                console.error(err);
            }
        },
    }
}
</script>

<style></style>