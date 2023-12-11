<script setup>
const props = defineProps(["Chaussure"]);
</script>

<template>
  <div>
    <div>
      <img
        class="float-left"
        :src="Chaussure['image.small']"
        alt="image of sneaker"
      />
    </div>

    <div class="mt-10">
      <div class="flex">
        
        <h5 class="font-black">Full name</h5>
        <p>: {{ Chaussure.name }}</p>
      </div>
      <br />
      <div class="flex">
        <h5 class="font-black">Brand</h5>
        <p>: {{ Chaussure.brand }}</p>
      </div>
      <br />
      <div class="flex">
        <h5 class="font-black">Colorway</h5>
        <p>: {{ Chaussure.colorway }}</p>
      </div>
      <br />
      <div class="flex">
        <h5 class="font-black">Release date</h5>
        <p>: {{ Chaussure.releaseDate }}</p>
      </div>
      <br />
      <div class="flex">
        <h5 class="font-black">Retail price</h5>
        <p>: {{ Chaussure.retailPrice }}$</p>
      </div>
      <br />
      <div class="flex">
        <h5 class="font-black">Estimated market value</h5>
        <p>: {{ Chaussure.estimatedMarketValue }}$</p>
      </div>
      <br />
      <div class="flex">
        <h5 class="font-black">Story</h5>
        <p class= "mr-100">: {{ Chaussure.story }}</p>
      </div>
      <div class="mt-10">
        <a
          :href="Chaussure['links.goat']"
          class="rounded-md bg-slate-900 px-5 py-2.5 font-bold text-white hover:bg-gray-700"
        >
          Buy Now
        </a>
      </div>
    </div>
  </div>
</template>
