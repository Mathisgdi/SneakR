<script setup>
const client = useSupabaseClient();
const router = useRouter();
const email = ref("");
const password = ref(null);
const errorMsg = ref(null);

async function signIn() {
    try{
        const {error} = await client.auth.signInWithPassword({
            email: email.value,
            password: password.value
        })
        if(error){
            throw error
        }
        else{
            router.push('/')
        }
    }
    catch(error){
        errorMsg.value = error.message
    }
}
</script>

<template>
    <div class="flex items-center justify-center min-h-screen bg-gray-100">
        <div class="bg-white p-8 rounded  shadow-md w150 h-auto">
            <h2 class="text-2xl font-bold mb-4">Login</h2>
            <form @submit.prevent="signIn">
                <div class="mb-4">
                    <label for="email" class="block text-gray-700 text-sm font-bold mb-2">
                        Email
                    </label>
                    <input type="email" id="email" class="w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:border-blue-500" placeholder="Your email address" v-model="email">
                </div>
                <div class="mb-4">
                    <label for="password" class="block text-gray-700 text-sm font-bold mb-2">
                        Password
                    </label>
                    <input type="password" id="password" class="w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:border-blue-500" placeholder="Your password" v-model="password">
                </div>
                <div>
                    <p v-if="errorMsg" class="text-red-500 text-xs italic">{{ errorMsg }}</p>
                </div>
                <button type="submit" class="w-full bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">SignIn</button>
                <div>
                    <p class="text-sm text-gray-500 mt-4">
                        Don't have an account? 
                        <NuxtLink to="/register" class="text-blue-500 hover:text-blue-700 text-xs italic">SignUp</NuxtLink>
                    </p>
                </div>
            </form>
        </div>
    </div>
</template>

