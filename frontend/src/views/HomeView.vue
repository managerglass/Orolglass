<template>
  <carrossel-component/>
  <sinopse-sobre-component />
  <servicos-component />
  <preview-obras-component />
</template>

<script>
import CarrosselComponent from '@/components/Carrossel/CarrosselComponent.vue'
import ServicosComponent from '@/components/Servicos/ServicosComponent.vue'
import PreviewObrasComponent from '@/components/Obras/PreviewObrasComponent.vue'
import SinopseSobreComponent from '@/components/Sobre/SinopseSobreComponent.vue'

export default {
  name: 'HomeView',
  components: {
    CarrosselComponent,
    ServicosComponent,
    PreviewObrasComponent,
    SinopseSobreComponent
  },

  data() {
    return {
      
    }
  }
}
</script>
