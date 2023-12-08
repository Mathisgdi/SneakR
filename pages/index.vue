<template>
    <div>
         <NuxtPage /> <!-- permet d'afficher le contenu de la page, ce base sur le dossier page -->
        <h1>Home page</h1>
        <!-- <button>
            <NuxtLink to="/profil">Profil</NuxtLink>
        </button>
        <button>
            <NuxtLink to="/register">Register</NuxtLink>
        </button>
        <button>
            <NuxtLink to="/login">Login</NuxtLink>
        </button> -->
        <section>
        <carte v-for="Chaussure in SneakR" :Chaussure= "Chaussure" />

        </section>
      
    </div>
</template>

<script setup lang="ts">
const client = useSupabaseClient()

const { data: SneakR } = await useAsyncData('SneakR', async () => {
const {data} = await client.from('SneakR').select('*').order('brand').range(0, 10)

return data})
console.log(SneakR.value)

</script>