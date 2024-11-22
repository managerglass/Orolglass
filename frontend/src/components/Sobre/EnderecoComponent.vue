<template>
    <div @click.prevent="gotoMaps(endereco.tipo)" class="flex flex-col md:flex-row justify-start px-4 py-6 md:justify-around border border-gray-300 gap-6 my-6 md:my-8 cursor-pointer">
        <h3 class="text-2xl font-bold text-azul_logo w-full">{{ endereco.tipo }}</h3>
        <div class="w-full">
            <label class="text-xl">Endereço</label>
            <p class="text-cor_texto">{{ endereco.endereco }}</p>
        </div>
        
        <div class="w-full">
            <label class="text-xl">Funcionamento</label>
            <p class="text-cor_texto">{{ endereco.funcionamento }}</p>
        </div>

    </div>
</template>

<script>

export default {
    name: 'EnderecoComponent',

    data() {
        return {

        }
    },

    props: {
        endereco: Object
    },


    methods: {
        gotoMaps(tipo) {
            if(tipo === 'Fábrica') {
                window.open('https://maps.app.goo.gl/CCWAvsWomzx4TsYN9', '_blank')
            } else if(tipo === 'Shoowroom') {
                window.open('https://maps.app.goo.gl/hyGo1kPEPPxDJbmS6', '_blank')
            } else {
                console.log('link nao existe');
            }
        }
    }
}

</script>

<style scopde lang="scss"></style>