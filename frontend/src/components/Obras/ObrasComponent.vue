<template>

</template>

<script>
export default {
    name: 'ObrasComponent',
    components: {
    },
    data() {
        return {
            images: [],
        }
    },

    created() {
        this.getImagesObras();
    },

    methods: {
        getImagesObras() {
            this.images = this.$store.state.imagensObras
        }
    }
}
</script>

<style></style>