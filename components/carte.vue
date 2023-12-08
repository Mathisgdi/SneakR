<template>
    <div class="carte">
      <img :src="Chaussure['image.small']" alt="">
      <h2>{{ Chaussure.name }}</h2>

    </div>
  </template>

<script setup>
const props = defineProps(["Chaussure"])
</script>