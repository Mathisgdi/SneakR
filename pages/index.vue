<template>
  <div>
    <NuxtPage />
    <search />
    <!-- permet d'afficher le contenu de la page, ce base sur le dossier page -->
    <section>
      <div
        class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4"
      >
        <carte v-for="Chaussure in SneakR" :Chaussure="Chaussure" />
      </div>
    </section>
    <UPagination class="flex justify-center items-center ml-5 mb-3 "
      :page-count="100"
      v-model="page"
      :total= "49214"
      :max="5"
    />
  </div>
</template>

<script setup lang="ts">

const page = ref(1);
// const items = ref([]);
const itemperpage = 100;
const client = useSupabaseClient();

const { data: SneakR } = await useAsyncData("SneakR", async () => {
  const { data } = await client
    .from("SneakR")
    .select("*")
    .range(page.value * itemperpage - itemperpage, page.value * itemperpage -1);
  return data;
});
console.log(SneakR.value);
watch(page, async  (newpage) => {
  const { data: SneakR } = await useAsyncData("SneakR", async () => {
  const { data } = await client
    .from("SneakR")
    .select("*")
    .range(page.value * itemperpage - itemperpage, page.value * itemperpage -1);
    window.scrollTo(0, 0)
  return data;
});})
</script>
