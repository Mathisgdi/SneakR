<template>
  <header class="flex justify-between items-center p-3">
    <div class="flex flex-row items-center gap-5 sm:gap-5 md:gap-5 lg:gap-10 ">
    <a href="/">
      <!-- <NuxtLink to="/"> J'ai enlevé le nuxt link car sinon la page ne se reload pas-->
      <img
        class="ml-5 h-10 w-auto"
        src="../img/SneakerLogo.avif"
        alt="Workflow"
      />
      <!-- </NuxtLink> -->
    </a>
    <NuxtLink to="/collection" >
      <button>Collection</button>
    </NuxtLink>
    <NuxtLink to="/wishlist">
      <button>Wishlist</button>
    </NuxtLink>
  </div>
    <div class="flex items-center">
      <UDropdown :items="items" mode="click">
        <UButton
          class="px-4 py-2 bg-indigo-600 text-white rounded hover:bg-indigo-500"
          trailing-icon="i-heroicons-chevron-down-20-solid"
        >
          Account
        </UButton>
        <template #item="{ item }">
          <span
            :class="{
              'text-red-500': item.label === 'Logout',
            }"
          >
            {{ item.label }}
          </span>
        </template>
      </UDropdown>
    </div>
  </header>
</template>
<script setup>
const user = useSupabaseUser();
const client = useSupabaseClient();
const router = useRouter();

let items = [];
if (!user.value) {
  items = [
    [
      {
        label: "Login",
        click: () => router.push("/login"),
      },
    ],
    [
      {
        label: "Register",
        click: () => router.push("/register"),
      },
    ],
  ];
} else {
  items = [
    [
      {
        label: "Logout",
        click: async () => {
          try {
            const { error } = await client.auth.signOut();
            if (error) {
              throw error;
            } else {
              reloadNuxtApp();
            }
          } catch (error) {
            console.log(error);
          }
        },
      },
    ],
  ];
}
</script>
