
<template>
  <UInput
    v-model="q"
    name="q"
    placeholder="Search..."
    icon="i-heroicons-magnifying-glass-20-solid"
    autocomplete="off"
    :ui="{ icon: { trailing: { pointer: '' } } }"
    class="flex items-center justify-center w-[80%] mx-auto"
  >
  </UInput>
</template>

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
