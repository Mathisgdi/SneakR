<script setup>
const client = useSupabaseClient();
const router = useRouter();
const email = ref("");
const password = ref(null);
const errorMsg = ref(null);

async function signIn() {
  try {
    const { error } = await client.auth.signInWithPassword({
      email: email.value,
      password: password.value,
    });
    if (error) {
      throw error;
    } else {
      router.push("/");
    }
  } catch (error) {
    errorMsg.value = error.message;
  }
}


definePageMeta({
  layout: 'empty'
})


</script>




<template>
  <div
    class="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8"
  >
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <!-- <NuxtImg src="/img/SneakerLogo.avif" placeholder="logo" /> -->
      <NuxtLink to="/">
        <img
          class="mx-auto h-20 w-auto"
          src="../public/img/SneakerLogo.avif"
          alt="Workflow"
        />
        <h2
          class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900"
        >
          Sign in to your account
        </h2>
      </NuxtLink>
    </div>

    <div class="mt-5 sm:mx-auto sm:w-full sm:max-w-sm">
      <form @submit.prevent="signIn" class="space-y-6" action="#" method="POST">
        <div>
          <label
            for="email"
            class="block text-sm font-medium leading-6 text-gray-900"
            >Email address</label
          >
          <div class="mt-2">
            <input
              id="email"
              name="email"
              type="email"
              autocomplete="email"
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder: pl-3 text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
              placeholder="Email address"
              v-model="email"
            />
          </div>
        </div>

        <div>
          <div class="flex items-center justify-between">
            <label
              for="password"
              class="block text-sm font-medium leading-6 text-gray-900"
              >Password</label
            >
            <div class="text-sm">
              <a
                href="#"
                class="font-semibold text-indigo-600 hover:text-indigo-500"
                >Forgot password?</a
              >
            </div>
          </div>
          <div class="mt-2">
            <input
              id="password"
              name="password"
              type="password"
              autocomplete="current-password"
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder: pl-3 text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
              placeholder="Password"
              v-model="password"
            />
          </div>
        </div>
        <div>
          <p v-if="errorMsg" class="text-red-500 text-xs italic">
            {{ errorMsg }}
          </p>
        </div>
        <div>
          <button
            type="submit"
            class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          >
            Sign in
          </button>
        </div>
      </form>

      <p class="mt-5 text-center text-sm text-gray-500">
        Don't have an account ?
        <NuxtLink
          to="/register"
          class="font-semibold leading-6 text-indigo-600 hover:text-indigo-500"
          >SignUp</NuxtLink
        >
      </p>
    </div>
  </div>
</template>
