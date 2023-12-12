<script setup>
const client = useSupabaseClient();
const email = ref(null);
const successMsg = ref(null);

async function resetPassword (){
  const { data, error } = await client.auth.resetPasswordForEmail(email.value, {
    redirectTo: 'http://localhost:3000/updatePassword',
    successMsg: 'Check your email for the password reset link.',

  })
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
      <NuxtLink to="/">
        <img
          class="mx-auto h-20 w-auto"
          src="../img/SneakerLogo.avif"
          alt="Workflow"
        />
        <h2
          class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900"
        >
          Reset Password
        </h2>
      </NuxtLink>
    </div>

    <div class="mt-5 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" action="#" method="POST">
        <div>
          <label
            for="email"
            class="block text-sm font-medium leading-6 text-gray-900"
            >Email</label
          >
          <div class="mt-2">
            <input
              id="email"
              name="email"
              type="email"
              autocomplete="email"
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder: pl-3 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
              placeholder="Email"
              v-model="email"
            />
          </div>
        </div>
        <div>
          <p v-if="successMsg" class="text-green-500 text-xs italic">
            {{ successMsg }}
          </p>
        </div>
        <div>
          <button
            type="submit"
            class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
            @click="resetPassword"
          >
            Reset
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
