<template>
  <h1>{{ details_sobre[0].sobre }}</h1>
  <h1>{{ sobre_valores[0].valor }}</h1>
  <h1>{{ sobre_crencas[0].crenca }}</h1>
</template>

<script>
export default {
  name: 'SobreComponent',

  data() {
    return {
      
    }
  },

  props: {
    details_sobre: {
      type: Object,
      required: true
    },
    sobre_valores: {
      type: Object,
      required: true
    },
    sobre_crencas: {
      type: Object,
      required: true
    }
  },

  created() {
    console.log(this.details_sobre);
  },

  methods: {

  }
}
</script>
<style lang="scss">

</style>
