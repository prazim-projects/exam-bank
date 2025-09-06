<template>
  <div class="max-w-md rounded-2xl shadow-md bg-white p-4 hover:shadow-lg transition">
    <!-- Title & Year -->
    <div class="flex justify-between items-center mb-2">
      <h2 class="text-lg font-semibold text-gray-800">
        {{ exam.title }}
      </h2>
      <span class="text-sm text-gray-500">{{ exam.year }}</span>
    </div>

    <!-- Upload Date & Visibility -->
    <p class="text-xs text-gray-500 mb-2">
      Uploaded: {{ formatDate(exam.uploadDate) }} | 
      <span class="capitalize">{{ exam.visibility }}</span>
    </p>

    <!-- File Download -->
    <div class="mb-3" v-for="filePath in exam.examFile" :key="filePath.id">
      <a 
        :href="`http://localhost:8000/media/${filePath.file}`" 
        target="blank" 
        class="text-blue-500 underline text-sm"
      >
        📄 View Exam File
      </a>
    </div>

    <!-- Difficulty Rating -->
    <div class="mb-2">
      <h3 class="text-sm font-medium text-gray-700">Difficulty Rating</h3>
      <div class="flex items-center gap-2">
        <span v-if="averageDifficulty !== null" class="text-yellow-500">
          ⭐ {{ averageDifficulty.toFixed(1) }}/5
        </span>
        <span v-else class="text-gray-400 text-sm">No ratings yet</span>
      </div>
    </div>

    <!-- Peer Reviews Count -->
    <p class="text-xs text-gray-600">
      {{ exam.difficultyratingSet?.length || 0 }} peer reviews
    </p>
  </div>
</template>

<script setup>
import { computed } from "vue";

const props = defineProps({
  exam: {
    type: Object,
    required: true,
  },
});

console.log("Exam prop:", props.exam);

// Format date
const formatDate = (date) => {
  return new Date(date).toLocaleDateString();
};

// Convert "A_3" -> 3
const parseDifficulty = (val) => {
  if (!val) return null;
  const num = val.split("_")[1];
  return Number(num) || null;
};

// Compute average difficulty
const averageDifficulty = computed(() => {
  const ratings = props.exam.difficultyratingSet || [];
  if (ratings.length === 0) return null;
  const parsed = ratings
    .map((r) => parseDifficulty(r.difficultyScore))
    .filter((n) => n !== null);
  if (parsed.length === 0) return null;
  return parsed.reduce((sum, n) => sum + n, 0) / parsed.length;
});
</script>
