<template>
    <div>
         <NuxtPage /> <!-- permet d'afficher le contenu de la page, ce base sur le dossier page -->
        <h1>Home page</h1>
        <button>
            <NuxtLink to="/profil">Profil</NuxtLink>
        </button>
    </div>
</template>

<script setup lang="ts">
const client = useSupabaseClient()

const { data: SneackR } = await useAsyncData('SneackR', async () => client.from('SneackR').select('*').order('brand').range(0, 10))

console.log(SneackR.value)

</script>