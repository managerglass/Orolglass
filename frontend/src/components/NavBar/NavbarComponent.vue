<template>
    <div class="header" :style="{ backdropFilter: blurEffect }">
        <div class="frame1">
            <div class="logo">
                <img class="w-40" src="../../assets/logo.svg" alt="Logo" />
            </div>
            <div class="frame1-dados">
                <button class="flex" @click.prevent="openLink('https://api.whatsapp.com/send?phone=55032999362017')">
                    <div>
                        <i class="fa-solid fa-phone text-2xl px-2"></i>
                    </div>
                    <div class="hidden md:block">
                        <p>(32) 99936 2017</p>
                    </div>
                </button>
                <button class="flex" @click.prevent="openLink('https://maps.app.goo.gl/hyGo1kPEPPxDJbmS6')">
                    <div>
                        <i class="fa-solid fa-location-dot text-2xl px-2"></i>
                    </div>
                    <div class="hidden md:block">
                        <p>Av. Dante Bruno, 335 - Dornelas/Muriaé-MG</p>
                    </div>
                </button>
            </div>
        </div>
        <div class="frame2-botoes" >
            <router-link v-for="link in links" :key="link.name" :to="link.path">{{ link.name }}</router-link>
        </div>
    </div>
</template>

<script>

export default {
    name: 'NavbarComponent',

    data() {
        return {
            links: [
                { name: 'Home', path: '/' },
                { name: 'Empresa', path: '/sobre' },
                { name: 'Obras', path: '/obras' },
                { name: 'Eventos', path: '/eventos' },
                { name: 'Contatos', path: '/contatos' }
            ],
            scrollY: 0
        }
    },

    methods: {
        openLink(link) {
            window.open(link, '_blank')
        }
    },

    computed: {
        blurEffect() {
            return this.scrollY > 0 ? 'blur(2px)' : 'none'
        }
    },

      mounted() {
    window.addEventListener('scroll', this.handleScroll);
  },

  beforeDestroy() {
    window.removeEventListener('scroll', this.handleScroll);
  },

  methods: {
    handleScroll() {
      this.scrollY = window.scrollY; // Update scroll position
    },
    openLink(link) {
      window.open(link, '_blank');
    },
  },
}

</script>

<style scoped lang="scss">
.header {
    @apply w-full px-6 md:px-24 divide-y-2 fixed top-0 z-50 text-white
}

.frame1 {
    @apply flex w-full justify-between py-8
}

.frame1-dados {
    @apply flex gap-8
}
.frame2 {
    @apply py-4
}
.frame2-botoes {
    @apply flex w-full justify-around py-5 md:text-xl
}
</style>