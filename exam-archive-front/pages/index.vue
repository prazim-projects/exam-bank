<script setup lang="ts">
</script>

<template>
  <div class="min-h-screen bg-gray-50 text-gray-800 p-6">
    <!-- Header Section -->
    <header class="mb-8 text-center">
      <h1 class="text-3xl font-bold mb-2">Selam Exam Archive</h1>
      <p class="text-gray-600">Your digital archive for past and upcoming exams</p>
    </header>

    <!-- Search / Input Section -->
    <section class="max-w-md mx-auto mb-8">
      <form class="bg-white shadow rounded-2xl p-6 space-y-4">
        <div>
          <label for="name" class="block text-sm font-medium text-gray-700">
            Search by Name
          </label>
          <input
            id="name"
            type="text"
            placeholder="Enter exam year or course name or code"
            class="mt-1 block w-full rounded-lg border border-gray-300 bg-gray-50 p-2 focus:border-blue-500 focus:ring-2 focus:ring-blue-400 outline-none"
          />
        </div>
        <button
          type="submit"
          class="w-full bg-blue-600 text-white py-2 rounded-lg shadow hover:bg-blue-700 transition"
        >
          Search
        </button>
      </form>
    </section>

    <!-- Content Section -->
    <section>
      <div
        class="bg-white rounded-2xl shadow p-6 flex flex-col items-center justify-center min-h-[200px]"
      >
        <p class="text-gray-500">📄 Content will appear here</p>
        <content />
      </div>
    </section>
  </div>
</template>
