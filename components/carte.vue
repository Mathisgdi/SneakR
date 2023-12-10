<script setup>
const props = defineProps(["Chaussure"]);
const isLiked = ref(false);
const isActive = ref(false);

function toggleLike() {
  isLiked.value = !isLiked.value;
}
function toggleHeart() {
  isActive.value = !isActive.value;
}
</script>

<template>
  <div
    class="relative m-10 flex w-full max-w-xs flex-col overflow-hidden rounded-lg border border-gray-100 bg-white shadow-md"
  >
    <!-- <NuxtLink to="detail"> -->
    <!-- <NuxtLink :to="`/detail/${Chaussure.id}`"> -->
      <a
        class="relative mx-3 mt-3 flex h-80 overflow-hidden rounded-xl"
        :href="`/detail/${Chaussure.id}`"
      >
        <img
          class="object-cover"
          :src="Chaussure['image.small']"
          alt="image of sneaker"
        />
      </a>
      <a href="#">
        <h5 class="text-xl mx-3 tracking-tight text-slate-900">
          {{ Chaussure.brand }}
          {{ Chaussure.silhouette }}
        </h5>
      </a>
    <!-- </NuxtLink> -->
    <div class="mt-4 px-5 pb-5">
      <div class="mt-2 mb-5 flex items-center justify-between">
        <p class="text-3xl font-bold text-slate-900">
          {{ Chaussure.estimatedMarketValue }}$
        </p>
        <!-- <button
          @click="toggleLike"
          :class="{
            'bg-red-500': isLiked,
            'bg-gray-300': !isLiked
          }"
          class="rounded-full w-10 h-10 flex items-center justify-center focus:outline-none"
        >
          <span class="text-red-500" v-if="isLiked">❤️</span>
          <span class="text-gray-300" v-else>🤍</span>
        </button> -->
    
        <div class="bg-[url('https://cssanimation.rocks/images/posts/steps/heart.png')] w-[100px] h-[100px] bg-cover transition-all duration-1000 steps-28 cursor-pointer"
        

        :class="{ 'is-active': isActive }"
        @click="toggleHeart">
          
        </div>
      </div>

      <a
        :href="Chaussure['links.goat']"
        class="flex items-center justify-center rounded-md bg-slate-900 px-5 py-2.5 text-center text-sm font-bold text-white hover:bg-gray-700"
      >
        Buy Now
      </a>
    </div>
  </div>
</template>

<style scoped>
.heart {
  width: 100px;
  height: 100px;
  background: url("https://cssanimation.rocks/images/posts/steps/heart.png") no-repeat;
  background-position: 0 0;
  cursor: pointer;
  transition: background-position 1s steps(28);
  transition-duration: 0s;
  
  &.is-active {
    transition-duration: 1s;
    background-position: -2800px 0;
  }
}


body {
  background: linear-gradient(135deg, #121721 0%, #000000 100%) fixed;
  color: #FFF;
  font: 300 16px/1.5 "Open Sans", sans-serif;
}

.stage {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>