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
                        Número para contato
                    </label>
                </div>

                <div class="relative w-full">
                    <textarea
                        class="py-2 outline-none border-2 focus:border-laranja_logo relative z-10 bg-transparent w-full"
                        placeholder=" " rows="5" v-model="relato"></textarea>
                    <label class="absolute left-0 top-2 transition-all duration-300 pointer-events-none"
                        :class="{ 'text-azul_logo text-xs': relato, '-top-2.5': relato }">
                        Número para contato
                    </label>
                </div>


            </div>
        </div>
    </div>


</template>

<script>

export default {
    name: 'NovaAvaliacao',

    data() {
        return {
            nome: '',
            numero: '',
            rede_social: ''

        }
    },

    methods: {
    }
}

</script>

<style scoped lang="scss"></style>