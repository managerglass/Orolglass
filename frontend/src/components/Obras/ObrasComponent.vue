<template>

<PreviewObrasComponent/>
</template>

<script>
import PreviewObrasComponent from './PreviewObrasComponent.vue'
export default {
    name: 'ObrasComponent',
    components: {
        PreviewObrasComponent
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