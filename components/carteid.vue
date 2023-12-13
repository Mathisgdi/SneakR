<template>
  <div class="grid sm:grid-cols-1 lg:grid-cols-2">
    <div>
      <img
        class="bg-gray-200"
        :src="Chaussure['image.small']"
        alt="image of sneaker"
      />
    </div>
    <div class="p-5">
      <div>
        <h5 class="font-black">Full name</h5>
        <p>{{ Chaussure.name }}</p>
      </div>
      <br />
      <div>
        <h5 class="font-black">Brand</h5>
        <p>{{ Chaussure.brand }}</p>
      </div>
      <br />
      <div>
        <h5 class="font-black">Colorway</h5>
        <p>{{ Chaussure.colorway }}</p>
      </div>
      <br />
      <div>
        <h5 class="font-black">Release date:</h5>
        <p>{{ Chaussure.releaseDate }}</p>
      </div>
      <br />
      <div>
        <h5 class="font-black">Retail price</h5>
        <p>{{ Chaussure.retailPrice }}$</p>
      </div>
      <br />
      <div>
        <h5 class="font-black">Estimated market value</h5>
        <p>${{ Chaussure.estimatedMarketValue }}</p>
      </div>
      <br />
      <div>
        <h5 class="font-black">Story</h5>
        <p class="mr-100">{{ Chaussure.story }}</p>
      </div>
      <div class="mt-10">
        <a
          :href="Chaussure['links.goat']"
          class="rounded-md px-5 py-2.5 font-bold text-white bg-indigo-600 hover:bg-indigo-500"
        >
          Buy Now
        </a>

        <button
          class="ml-5 inline-flex items-center justify-center w-10 h-10 mr-2 text-indigo-100 transition-colors duration-150 rounded-lg focus:shadow-outline hover:bg-indigo-600"
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
        <div>
          <button
            class="heart"
            @click="toggleHeart"
            :class="{ 'is-active': isActive }"
          ></button>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
const props = defineProps(["Chaussure"]);
const isActive = ref(false);
const isClicked = ref(false);
const user = useSupabaseUser();

function toggleHeart() {
  if (!user.value) {
    alert("You must be login to add to whislist");
    return;
  } else {
    isActive.value = !isActive.value;
  }
}
function toggleClick() {
  if (!user.value) {
    alert("You must be login to add to collection");
    return;
  } else {
    isClicked.value = !isClicked.value;
  }
}
</script>
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
