<script setup lang="ts">

const client = useSupabaseClient();
const route = useRoute()
const idpage = ref(null);
const idpagenumber = route.params.id
 
const { data: SneakR } = await useAsyncData("SneakR", async () => {
  const { data } = await client
    .from("SneakR")
    .select("*")
    .eq("id", route.params.id);

  return data;
});
console.log(SneakR.value);

definePageMeta({
  layout: 'empty'
})
</script>

<template>
  <div v-if="typeof idpagenumber === 'string'">
    toto
    <NuxtPage />
    <!-- permet d'afficher le contenu de la page, ce base sur le dossier page -->
    <div>
      <carteid {{ route.params.id }} />

    </div>
    <!-- <pre>{{ route }}</pre> -->
  </div>
</template>

