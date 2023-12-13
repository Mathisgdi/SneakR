<template>
  <div class="flex flex-col items-center justify-center h-screen bg-gray-100">
    <h1 class="text-3xl font-bold mb-4">Profil Page</h1>
    <!-- <h1 class="text-xl mb-2">Email: {{ user.email }}</h1> -->
    <div>
      <p v-if="errorMsg" class="text-red-500 text-xs italic">{{ errorMsg }}</p>
    </div>
    <button
      @click="logout"
      type="button"
      class="bg-red-500 text-white py-2 px-4 rounded hover:bg-red-600"
    >
      Logout
    </button>
  </div>
</template>

<script setup>
const user = useSupabaseUser(); // Récupère l'utilisateur connecté et ses informations
const client = useSupabaseClient();
const router = useRouter();
const errorMsg = ref(null);

async function logout() {
  try {
    const { error } = await client.auth.signOut();
    if (error) {
      throw error;
    } else {
      router.push("/");
    }
  } catch (error) {
    console.log(error);
    errorMsg.value = error.message;
  }
}
</script>