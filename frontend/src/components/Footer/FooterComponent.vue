<template>
    <div class="conatiner-footer">
        <div class="footer">
            <div class="coluna1">
                <div>
                    <img class="w-32" src="../../assets/logo.svg" alt="Logo do site"/>
                </div>
                <p>Somos uma empresa de relacionamento com o cliente, que por acado comercializamos vidros e fabricamos esquadrias de alto padrão.</p>
                <div class="icones">
                    <button @click.prevent="openLink('https://api.whatsapp.com/send?phone=55032999362017')">
                        <i class="fa-brands fa-whatsapp"></i>
                    </button>
                    <button @click.prevent="openLink('https://www.instagram.com/orolglass/')">
                        <i class="fa-brands fa-instagram"></i>
                    </button>
                    <button @click.prevent="openLink('https://www.facebook.com/orolglass')">
                        <i class="fa-brands fa-facebook"></i>
                    </button>
                </div>
            </div>
            <div class="coluna2">
                <h3 class="text-xl font-bold">Institucional</h3>
                <ul>
                    <li>Home</li>
                    <li>Empresa</li>
                    <li>Obras</li>
                    <li>Eventos</li>
                    <li>Contatos</li>
                </ul>
            </div>
            <div class="coluna3">
                <h3>Links Rápidos</h3>
                <ul>
                    <li>Maps Fábrica</li>
                    <li>Comercial</li>
                    <li>Vendas</li>
                    <li>Portifólio de Produtos</li>
                    <li>Obras Finalizadas</li>
                </ul>
            </div>
            <div class="coluna4">
                <h3>Testando</h3>
                <p>Usando texto de teste</p>
                <button>Testaiada</button>
            </div>
        </div>
        <div class="direitos-reservadors">
            <p>&copy; 2024 Desenvolvido por Orolglass</p>
        </div>
    </div>                                                                                              
    
</template>

<script>

export default {
    name: 'FooterComponent',

    data() {
        return {

        }
    },

    methods: {
        openLink(link) {
            window.open(link, '_blank')
        }
    }
}

</script>

<style scoped lang="scss">
/* css container footer pai */
.container-footer {
    @apply flex bg-cor_fundo w-full
}                                       

/* css container infos footer */                                                              
.footer {
    @apply flex justify-around bg-cor_fundo py-16 flex-col md:flex-row gap-12 md:gap-12 px-6 md:px-24                                                         
}

.icones {
    @apply flex gap-6 text-xl text-white
}

.coluna1 {
    @apply flex flex-col gap-4 text-white font-semibold w-full
}

.coluna2 {
    @apply flex flex-col gap-4 text-white w-full
}
.coluna3 {
    @apply flex flex-col gap-4 text-white w-full
}
.coluna4 {
    @apply flex flex-col gap-4 text-white w-full
}


/* css dos direitos reservados */     
.direitos-reservadors {
    @apply flex w-full justify-center items-center py-6 font-semibold text-sm md:text-base
}

</style>