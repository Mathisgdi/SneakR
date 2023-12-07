<script setup>
const client = useSupabaseClient()
const email = ref("");
const password = ref (null);
const errorMsg = ref (null);
const successMsg = ref(null);

async function signUp() {
    console.log('signUp function called'); 
    try{
        const {data, error} = await client.auth.signUp({
            email: email.value,
            password: password.value
        })
        if(error){
            throw error 
        }
        else{
            successMsg.value = "Check your email to confirm your account"
        } 
    }
    catch(error){
        errorMsg.value = error.message
    }

}


</script>

<template>
    <div class="flex justify-center items-center h-screen">
        <form @submit.prevent="signUp" class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
            <div class="mb-4">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="username">
                    Email
                </label>
                <input
                    class="shadow appearance-none border rounded-lg w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    id="email"
                    type="email"
                    placeholder="Enter your email"
                    v-model="email"
                />
            </div>
            <div class="mb-4">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="password">
                    Password
                </label>
                <input
                    class="shadow appearance-none border rounded-lg w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
                    id="password"
                    type="password"
                    placeholder="Enter your password"
                    v-model="password"
                />
            </div>
            <div class="error">
                <p v-if="errorMsg" class="text-red-500 text-xs italic">{{ errorMsg }}</p>
            </div>
            <div>
                <p v-if="successMsg" class="text-green-500 text-xs italic">{{ successMsg }}</p>
            </div>
            <div class="flex items-center justify-between">
                <button
                    class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                    type="submit"
                >
                    SignUp
                </button>
            </div>
            <div>
                <p class="text-gray-700 text-xs mt-3">Already have an account?
                <NuxtLink to="/login" class="text-blue-500 hover:text-blue-700 text-xs italic">Login</NuxtLink>
            </p>
            </div>
            
        </form>
    </div>
</template>

