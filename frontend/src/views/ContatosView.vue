<template>
    <div>
        <div class="bg-cover absolute left-0 right-0 top-0 -z-10 bottom-0 h-[30vh] md:h-[30vh]"
            :style="{ backgroundImage: 'url(http://192.168.18.88:8000/media/imagens/3_8qdtQcf_ocLULKX.jpg)' }">
        </div>
        <div class="bg-cover bg-black/20 absolute left-0 right-0 top-0 -z-10 bottom-0 h-[30vh] md:h-[30vh]">
        </div>
        <div class="container-section mt-40">
            <h1 class="title-section pb-8 text-center bg-white w-52 mx-auto pt-2">CONTATOS</h1>
            <div class="flex flex-col md:flex-row w-full justify-around">
                <div class="flex flex-col w-full gap-5 p-4">
                    <ContatosComponent :contato="contato" v-for="contato in contatos" :key="contato.id" />
                </div>
                <div class="flex flex-col gap-10 p-4 w-full">
                    <h1 class="text-2xl text-azul_logo">Enviar <span class="text-laranja_logo">Mensagem</span></h1>
                    <form class="flex flex-col gap-8">
                        <div class="relative w-full">
                            <input
                                class="py-2 outline-none border-b-2 focus:border-laranja_logo relative z-10 bg-transparent w-full"
                                type="text" placeholder=" " v-model="nome" />
                            <label class="absolute left-0 top-2 transition-all duration-300 pointer-events-none"
                                :class="{ 'text-azul_logo text-xs': nome, '-top-3': nome }">
                                Nome Completo
                            </label>
                        </div>

                        <div class="relative w-full">
                            <input
                                class="py-2 outline-none border-b-2 focus:border-laranja_logo relative z-10 bg-transparent w-full"
                                type="email" placeholder=" " v-model="email" />
                            <label class="absolute left-0 top-2 transition-all duration-300 pointer-events-none"
                                :class="{ 'text-azul_logo text-xs': email, '-top-3': email }">
                                E-mail
                            </label>
                        </div>

                        <div class="relative w-full">
                            <select
                                class="py-2 outline-none border-b-2 focus:border-laranja_logo relative z-10 bg-transparent w-full"
                                v-model="numero">
                                <option value="" disabled selected hidden></option>
                                <!-- Adicione opções conforme necessário -->
                                <option value="55032999362017">Comercial</option>
                                <option value="55032998502027">Vendas</option>
                                <option value="55032988607060">Fábrica</option>
                                <option value="55032998061820">Técnico</option>
                                <option value="55032984923475">Manutenção</option>
                            </select>
                            <label class="absolute left-0 top-2 transition-all duration-300 pointer-events-none"
                                :class="{ 'text-azul_logo text-xs': numero, '-top-3': numero }">
                                Falar com
                            </label>
                        </div>

                        <div class="relative w-full">
                            <textarea
                                class="py-2 px-2 outline-none border-2 focus:border-laranja_logo relative z-10 bg-transparent w-full"
                                placeholder="Avaliação" rows="5" maxlength="500" v-model="assunto"></textarea>
                        </div>

                        <div class="w-full">
                            <button @click="pushMessage" class="text-center font-bold bg-cor_fundo text-white py-2 w-full">Enviar</button>
                        </div>

                    </form>
                </div>
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
            assunto: '',
            numero: ''
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
        },

        async pushMessage() {
            try {
                const url = `https://api.whatsapp.com/send?phone=${this.numero}&text=Nome:%20${this.nome}%0AE-mail:%20${this.email}%0A%0AAssunto:%0A${this.assunto}`
                window.open(url, '_blank')
            } catch(err) {
                console.error(err);
            }
        }
    }
}

</script>

<style scoped lang="scss"></style>