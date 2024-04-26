<template>

  <div class="container-section">
    <h1 class="title-section">Nossos <span>Serviços</span></h1>
    <div class="container-services">
      <div v-for="service in services" :key="service.id" class="service" >
        <i class="text-4xl" :class="service.icone"></i>
        <h1 class="text-xl text-azul_logo mb-6">{{ service.titulo }}</h1>
        <p>{{ service.descricao }}</p>
        <div class="w-full flex justify-end px-10 mt-4">
          <span class="text-5xl font-bold text-cor_texto">{{ service.id }}</span>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
export default {
  name: 'ServicosComponent',

  data() {
    return {
      services: [
        {
          icone: 'fa-solid fa-city',
          titulo: 'ESQUADRIAS',
          descricao: 'Os sistemas mais modernos de esquadrias de alto padrão.',
          id: '01'
        },
        {
          icone: 'fa-solid fa-shop',
          titulo: 'DESIGN INTERIOR',
          descricao: 'Melhor design de escadas e espelhos para aumentar a valorização do ambiente do seu lar.',
          id: '02'
        },
        {
          icone: 'fa-solid fa-city',
          titulo: 'ESPECIAIS',
          descricao: 'Glazing(Pele de vidros), visor e fundos de piscinas com vidro múlti-laminados temperado.',
          id: '03'
        },
      ]
    }
  }
}
</script>

<style lang="scss">
.container-section {
  @apply bg-transparent md:px-24 py-12 md:pt-24
}

.title-section {
  @apply text-3xl md:text-4xl w-full text-center md:text-start md:px-6 font-bold text-azul_logo
}

.title-section span {
  @apply text-laranja_logo
}

.container-services {
  @apply flex flex-col gap-8 md:flex-row px-6 py-12
}

.service {
  @apply w-full flex flex-col gap-3 px-6 py-12 bg-slate-50
}
</style>
