<template>
  <div>
    <NuxtPage />
    collection de l'utilisateur
    <!-- <section>
      <div>
        <carteid v-for="Chaussure in SneakR" :Chaussure="Chaussure" />
      </div>
    </section> -->
  </div>
</template>

<!-- <script>

defineProps(["Chaussure"]);
function idChaussure() {
  for ( var chausure in  user.value.user_metadata.collection)
  return chausure; {
    return ;
  }
}
const user = useSupabaseUser();

const client = useSupabaseClient();
const route = useRoute();
let collectionUser = user.value.user_metadata.collection;
const collectionUserIdChaussure = user.value.user_metadata.collection;
const { data: SneakR } = await useAsyncData("SneakR", async () => {
  const { data } = await client
    .from("SneakR")
    .select("*")
    .order("brand")
    .eq("id", idChaussure());

  return data;
});
</script> -->
