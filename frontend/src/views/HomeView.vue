<template>
  <carrossel-component/>
  <sinopse-sobre-component />
  <servicos-component />
  <preview-obras-component />
  <avaliacoes-component />
</template>

<script>
import CarrosselComponent from '@/components/Carrossel/CarrosselComponent.vue'
import ServicosComponent from '@/components/Servicos/ServicosComponent.vue'
import PreviewObrasComponent from '@/components/Obras/PreviewObrasComponent.vue'
import SinopseSobreComponent from '@/components/Sobre/SinopseSobreComponent.vue'
import AvaliacoesComponent from '@/components/Avaliacoes/AvaliacoesComponent.vue'

export default {
  name: 'HomeView',
  components: {
    CarrosselComponent,
    ServicosComponent,
    PreviewObrasComponent,
    SinopseSobreComponent,
    AvaliacoesComponent
  },

  data() {
    return {
      
    }
  }
}
</script>
