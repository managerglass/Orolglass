<template>

    <div class="container-section">
        <h1 class="title-section">Contatos</h1>
        <div v-for="contato in contatos" :key="contato.id">
            <ContatosComponent :contato="contato" />
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
            contatos: []
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