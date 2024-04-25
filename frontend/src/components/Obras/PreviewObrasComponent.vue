<template>

    <div class="container-section">
        <h1 class="title-section">Algumas <span>Obras</span></h1>

        <div
            class="overflow-x-hidden flex gap-24">
            <div v-for="(projeto, index) in projects" :key="projeto.id">
                <div class="w-full h-full bg-cover" :style="{background: `url(${projeto.arquivo})`}">

                </div>
                <p>{{ projeto.titulo }}</p>
            </div>
            
        </div>
    </div>

</template>

<script>

export default {
    name: 'PreviewObrasComponent',

    data() {
        return {
            projects: [],
            projetoAtual: ''
        }
    },

    created() {
        this.getProjects()
    },

    methods: {
        async getProjects() {
            this.projects = this.$store.state.imagensDestques
        }
    }
}

</script>

<style scoped lang="scss">

</style>