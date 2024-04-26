<template>

    <div class="container-section">
        <h1 class="title-section">Algumas <span>Obras</span></h1>
        <div class=" w-full overflow-x-scroll h-96 flex gap-6 px-6 py-8">
            <div v-for="(projeto) in projects" :key="projeto.id" class="relative">
                <div class="w-72 h-60 "
                    :style="{ background: `url(${projeto.arquivo})`, backgroundSize: 'cover', backgroundPosition: 'center' }">
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

<style scoped lang="scss"></style>