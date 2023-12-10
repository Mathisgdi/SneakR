<template>
  <div>
    <NuxtPage />
    <!-- permet d'afficher le contenu de la page, ce base sur le dossier page -->
    <section>
      <div
        class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-2"
      >
        <carte v-for="Chaussure in SneakR" :Chaussure="Chaussure" />
      </div>
    </section>
    <UPagination
      :max="5"
      v-model="page"
      :page-count="5"
      :total="items.length"
    />
  </div>
</template>

<script setup lang="ts">
const page = ref(0);
const itemperpage = ref(10);
const items = ref(Array(55));
const client = useSupabaseClient();

const { data: SneakR } = await useAsyncData("SneakR", async () => {
  const { data } = await client
    .from("SneakR")
    .select("*")
    .order("brand")
    // .range(page.value, page.value + itemperpage.value);
    .range(20000,20050)

  return data;
});
console.log(SneakR.value);
</script>
