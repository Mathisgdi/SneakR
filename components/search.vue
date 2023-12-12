<script>
const searchcontent = ref("");

async function search() {
  console.log("search");
  const { data: SneakR } = await useAsyncData("SneakR", async () => {
    const { data } = await client
      .from("SneakR")
      .select("*")
      .ilike("name", '%${searchcontent.value}%');
    return data;
  });
}

</script>

<template>
  <div class="flex justify-center items-center">
    <input
      v-model="searchcontent"
      type="text"
      placeholder="Search a sneaker"
      class="flex items-center rounded-md"
    />
    <button @click="search">
      <img src="../img/iconSearch.svg" alt="search icon" class="w-9" />
    </button>
  </div>
</template>
