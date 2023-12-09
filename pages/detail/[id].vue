<template>
  <div>
    <NuxtPage />
    <!-- permet d'afficher le contenu de la page, ce base sur le dossier page -->
    <div>
      <carteid {{ $route.params.id }} />

    </div>
    <!-- <pre>{{ route }}</pre> -->
  </div>
</template>

<script setup lang="ts">

const client = useSupabaseClient();
const route = useRoute()
console.log(route.params.id);

const { data: SneakR } = await useAsyncData("SneakR", async () => {
  const { data } = await client
    .from("SneakR")
    .select("*")
    .eq("id", route.params.id);

  return data;
});


definePageMeta({
  layout: 'empty'
})
</script>
