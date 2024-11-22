<template>

    <div class="flex gap-3">
        <strong class="text-laranja_logo">{{ contato.titulo }}:</strong><span class="text-cor_texto">{{ contato.contato }}</span>
    </div>

</template>

<script>

export default {
    name: 'ContatosComponent',

    data() {
        return {

        }
    },

    props: {
        contato: Object,
    },

    methods: {

    },
}

</script>

<style scoped lang="scss">

</style>