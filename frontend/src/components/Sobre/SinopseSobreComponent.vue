<template>

{{ sinopse.sobre }}

</template>

<script>
import axios from 'axios'
export default {
    name: 'SinopseSobreComponent',

    data() {
        return {
            sinopse: ''
        }
    },

    mounted() {
        this.getSobreSinopse()
    },

    methods: {
        async getSobreSinopse() {
            try {
                const response = await axios.get(`${this.$store.state.BASE_URL}sobre/`)
                this.sinopse = response.data[0]
            } catch (err) {
                console.error(err);
            }
        }
    }

}

</script>

<style scoped lang="scss"></style>