<script lang="ts" setup>

</script>

<template>

<div class="grid grid-cols-3 gap-6 p-6">
    <div
      v-for="exam in result?.exams"
      :key="exam.id"
      class="p-4 bg-white shadow-md rounded-xl cursor-pointer hover:shadow-lg"
      @click="goToExam(exam.id)"
    >
      <h2 class="text-lg font-semibold">{{ exam.title }}</h2>
      <p class="text-gray-600 text-sm">{{ exam.description }}</p>
    </div>
</div>

  <div v-if="loading">Loading exams...</div>
  <div v-if="error">{{ error.message }}</div>
    
</template>