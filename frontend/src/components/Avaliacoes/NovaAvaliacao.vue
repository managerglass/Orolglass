<template>

    <div class="fixed z-50 top-0 left-0 right-0 bottom-0 bg-black/40">
        <div class="flex justify-center items-center h-screen">
            <div class="bg-white shadow-xl flex flex-col w-full mx-4 h-[70%] px-4 gap-6">
                <div class="flex justify-between w-full text-xl py-4">
                    <h1>Nova Avaliação</h1>
                    <button @click="$emit('fechar')"><i class="fas fa-xmark"></i></button>
                </div>
                <div class="relative w-full">
                    <input
                        class="py-2 outline-none border-b-2 focus:border-laranja_logo relative z-10 bg-transparent w-full"
                        type="text" placeholder=" " v-model="nome" />
                    <label class="absolute left-0 top-2 transition-all duration-300 pointer-events-none"
                        :class="{ 'text-azul_logo text-xs': nome, '-top-2.5': nome }">
                        Nome
                    </label>
                </div>
                <div class="relative w-full">
                    <input
                        class="py-2 outline-none border-b-2 focus:border-laranja_logo relative z-10 bg-transparent w-full"
                        type="text" placeholder=" " v-model="numero" />
                    <label class="absolute left-0 top-2 transition-all duration-300 pointer-events-none"
                        :class="{ 'text-azul_logo text-xs': numero, '-top-2.5': numero }">
                        Número para contato
                    </label>
                </div>
                <div class="relative w-full">
                    <select
                        class="py-2 outline-none border-b-2 focus:border-laranja_logo relative z-10 bg-transparent w-full"
                        v-model="rede_social">
                        <option value="" disabled selected hidden></option>
                        <!-- Adicione opções conforme necessário -->
                        <option value="FACEOOK">Facebook</option>
                        <option value="WHATSAPP">Whatsapp</option>
                        <option value="INSTAGRAM">Instagram</option>
                    </select>
                    <label class="absolute left-0 top-2 transition-all duration-300 pointer-events-none"
                        :class="{ 'text-azul_logo text-xs': rede_social, '-top-2.5': rede_social }">
                        Onde nos conheceu?
                    </label>
                </div>

                <div class="relative w-full">
                    <textarea
                        class="py-2 px-2 outline-none border-2 focus:border-laranja_logo relative z-10 bg-transparent w-full"
                        placeholder="Avaliação" rows="5" maxlength="200"
                         v-model="relato"></textarea>
                </div>

                <div >
                    <button @click.prevent="novaAvaliacao()" class="bg-cor_fundo w-full text-center text-white font-bold py-2">Enivar Avaliação</button>
                </div>
            </div>
        </div>
    </div>


</template>

<script>
import axios from 'axios'

export default {
    name: 'NovaAvaliacao',

    data() {
        return {
            nome: '',
            numero: '',
            rede_social: '',
            relato: ''

        }
    },

    methods: {
        async novaAvaliacao() {
            try {
                const data = {
                    nome: this.nome,
                    rede_social: this.rede_social,
                    relato: this.relato,
                    contato: this.numero
                }
                const res = await axios.post(`${this.$store.state.BASE_URL}avaliacoes/`, data)
                this.$emit('fechar')
                this.$emit('atualizar')

            }catch(err) {
                console.error(err);
            }
        }
    }
}

</script>

<style scoped lang="scss"></style>