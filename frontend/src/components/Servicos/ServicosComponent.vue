<template>

  <div class="container-section hidden md:block">
    <h1 class="title-section">Nossos <span>Serviços</span></h1>
    <div class="container-services">
      <div v-for="service in services" :key="service.id" class="service">
        <i class="text-4xl" :class="service.icone"></i>
        <h1 class="text-xl text-azul_logo mb-6">{{ service.titulo }}</h1>
        <p>{{ service.descricao }}</p>
        <div class="w-full flex justify-end px-10 mt-4">
          <span class="text-5xl font-bold text-cor_texto">{{ service.id }}</span>
        </div>
      </div>
    </div>
  </div>

  <div class="block md:hidden">
    <h1 class="title-section py-6">Nossos <span>Serviços</span></h1>
    <div class="flex items-start justify-start w-full h-52 mb-12">
      <div class="w-44 h-full bg-slate-50 flex flex-col p-4 justify-between">
        <i :class="services[0].icone" class="text-4xl text-cor_texto"></i>
        <span class="text-4xl font-bold text-cor_texto text-end">{{ services[0].id }}</span>
      </div>
      <div class="flex flex-col w-full ml-10 gap-6 my-2">
        <h1 class="text-3xl text-azul_logo">{{ services[0].titulo }}</h1>
        <p class="text-xl">{{ services[0].descricao }}</p>
      </div>
    </div>

    <div class="flex items-start justify-start w-full h-52 mb-12">
      <div class="flex flex-col w-full ml-10 gap-6 my-2">
        <h1 class="text-3xl text-azul_logo">{{ services[1].titulo }}</h1>
        <p class="text-xl">{{ services[1].descricao }}</p>
      </div>
      <div class="w-44 h-full bg-slate-50 flex flex-col p-4 justify-between">
        <i :class="services[1].icone" class="text-4xl text-cor_texto"></i>
        <span class="text-4xl font-bold text-cor_texto text-end">{{ services[1].id }}</span>
      </div>
    </div>

    <div class="flex items-start justify-start w-full h-52">
      <div class="w-44 h-full bg-slate-50 flex flex-col p-4 justify-between">
        <i :class="services[2].icone" class="text-4xl text-cor_texto"></i>
        <span class="text-4xl font-bold text-cor_texto text-end">{{ services[2].id }}</span>
      </div>
      <div class="flex flex-col w-full ml-10 gap-6 my-2">
        <h1 class="text-3xl text-azul_logo">{{ services[2].titulo }}</h1>
        <p class="text-xl">{{ services[2].descricao }}</p>
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
