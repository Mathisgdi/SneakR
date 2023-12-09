<script setup>
const user = useSupabaseUser();
</script>

<template>
  <header class="flex justify-between items-center p-3 ">
    <NuxtLink to="/">
      <img
        class="ml-10 h-10 w-auto"
        src="../img/SneakerLogo.avif"
        alt="Workflow"
      />
    </NuxtLink>

    <div class="flex items-center">
      <button
        v-if="user?.value"
        class="px-4 py-2 bg-blue-500 text-white"
      >
        <NuxtLink to="/profil">Profil</NuxtLink>
      </button>
      <button v-else class="px-4 py-2 bg-blue-500 text-white">
        <NuxtLink to="/login">Login</NuxtLink>
      </button>
    </div>
  </header>
</template>
