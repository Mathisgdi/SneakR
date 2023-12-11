<template>
  <div>
    <NuxtPage />
    <section>
      <div>
        <carteid v-for="Chaussure in SneakR" :Chaussure="Chaussure" />
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
const client = useSupabaseClient();
const route = useRoute();
const idpage = ref(null);
const idpagenumber = route.params.id;


const { data: SneakR } = await useAsyncData("SneakR", async () => {
  const { data } = await client
    .from("SneakR")
    .select("*")
    .order("brand")
    // .range(page.value, page.value + itemperpage.value);
    .eq("id", route.params._id);

  return data;
});
console.log(SneakR.value);
console.log("test");
console.log(route.params._id);

// definePageMeta({
//   layout: "empty",
// });
const props = defineProps(["Chaussure"]);
</script>
