<template>

    <div class="container-section">
        <h1 class="title-section pb-8 text-center">Contatos</h1>
        <div class="flex flex-col md:flex-row w-full justify-around">
            <div class="flex flex-col w-full gap-5 p-4">
                <ContatosComponent :contato="contato" v-for="contato in contatos" :key="contato.id" />
            </div>
            <div class="flex flex-col gap-10 p-4 w-full">
                <h1 class="text-2xl text-azul_logo">Enviar Mensagem</h1>
                <form class="flex flex-col gap-8">
                    <div class="relative w-full">
                        <input
                            class="py-2 outline-none border-b-2 focus:border-laranja_logo relative z-10 bg-transparent w-full"
                            type="text" placeholder=" " v-model="nome" />
                        <label class="absolute left-0 top-2 transition-all duration-300 pointer-events-none"
                            :class="{ 'text-azul_logo text-xs': nome, '-top-2': nome }">
                            Nome Completo
                        </label>
                    </div>


                    <div class="relative w-full">
                        <input
                            class="py-2 outline-none border-b-2 focus:border-laranja_logo relative z-10 bg-transparent w-full"
                            type="email" placeholder=" " v-model="email" />
                        <label class="absolute left-0 top-2 transition-all duration-300 pointer-events-none"
                            :class="{ 'text-azul_logo text-xs': email, '-top-2': email }">
                            E-mail
                        </label>
                    </div>

                    <div class="flex flex-col">
                        <label>Assunto</label>
                        <textarea v-model="assunto" />
                    </div>

                    <div class="w-full">
                        <button class="">Enviar</button>
                    </div>

                </form>
            </div>
        </div>
    </div>

</template>

<script>
import axios from 'axios'
import ContatosComponent from '../components/Contatos/ContatosComponent.vue'
export default {
    name: 'ContatosView.vue',

    components: {
        ContatosComponent
    },
    data() {
        return {
            contatos: [],
            email: '',
            nome: '',
            assunto: ''
        }
    },

    mounted() {
        this.getContatos()
    },

    methods: {
        async getContatos() {
            try {
                const response = await axios.get(`${this.$store.state.BASE_URL}contatos/`)
                this.contatos = response.data
                console.log(this.contatos);
            } catch (err) {
                console.error(err);
            }
        }
    }
}

</script>

<style scoped lang="scss"></style>