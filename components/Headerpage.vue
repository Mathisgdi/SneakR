<script setup>
const user = useSupabaseUser();
</script>

<template>
  <header class="flex justify-between items-center p-3 ">
    <a href="/">
    <!-- <NuxtLink to="/"> J'ai enlevé le nuxt link car sinon la page ne se reload pas-->
      <img
        class="ml-10 h-10 w-auto"
        src="../img/SneakerLogo.avif"
        alt="Workflow"
      />
    <!-- </NuxtLink> -->
  </a>
    <div class="flex items-center">
      <button
        v-if="user?.value"
        class="px-4 py-2 bg-blue-500 text-white"
      >
        <NuxtLink to="/profil">Profil</NuxtLink>
      </button>
      <button v-else class="px-4 py-2 bg-indigo-600 text-white rounded hover:bg-indigo-500">
        <NuxtLink to="/login">Login</NuxtLink>
      </button>
    </div>
  </header>
</template>
