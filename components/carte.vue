<script setup>
const props = defineProps(["Chaussure"]);
const isActive = ref(false);
const isClicked = ref(false);

function toggleHeart() {
  isActive.value = !isActive.value;
}
function toggleClick() {
  isClicked.value = !isClicked.value;
}
</script>

<template>
  <div
    class="relative m-5 flex w-full max-w-xs flex-col overflow-hidden rounded-lg border border-gray-100 bg-white shadow-md"
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
        <div
          class="heart"
          @click="toggleHeart"
          :class="{ 'is-active': isActive }"
        ></div>

        <button
          class="inline-flex items-center justify-center w-10 h-10 mr-2 text-indigo-100 transition-colors duration-150 rounded-lg focus:shadow-outline hover:bg-indigo-600"
          :class="{ 'bg-indigo-600': isClicked, 'bg-slate-300': !isClicked }" 
          @click="toggleClick"
        >
          <svg class="w-4 h-4 fill-current" viewBox="0 0 20 20">
            <path
              d="M10 3a1 1 0 011 1v5h5a1 1 0 110 2h-5v5a1 1 0 11-2 0v-5H4a1 1 0 110-2h5V4a1 1 0 011-1z"
              clip-rule="evenodd"
              fill-rule="evenodd"
            ></path>
          </svg>
        </button>
      </div>
      <a
        :href="Chaussure['links.goat']"
        class="flex items-center justify-center rounded-md bg-indigo-600 hover:bg-indigo-500 px-5 py-2.5 text-center text-sm font-bold text-white"
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
  background: url("https://cssanimation.rocks/images/posts/steps/heart.png")
    no-repeat;
  background-position: 0 0;
  cursor: pointer;
  transition: background-position 1s steps(28);
  transition-duration: 0s;

  &.is-active {
    transition-duration: 1s;
    background-position: -2800px 0;
  }
}
</style>
