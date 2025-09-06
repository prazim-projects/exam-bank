<script setup lang="ts">
import { useQuery } from "@vue/apollo-composable"
import gql from "graphql-tag"
import { ref } from "vue"
import { useUserStore } from "@/stores/user.store"

// Store (already has the logged-in user info)
const userStore = useUserStore()

// GraphQL Query: fetch user by ID
const GET_USER = gql`
  query GetUser($id: String!) {
    userById(id: $id) {
      id
      username
      email
      role
      studentID
    }
  }
`

const { result, loading, error } = useQuery(GET_USER, {
  id: userStore.loggedUser?.id // user ID from Pinia store
})

const user = ref(null)

watch(result, (val) => {
  if (val?.userById) {
    user.value = val.userById
  }
})
</script>

<template>
  <div class="min-h-screen bg-gray-50 p-6">
    <!-- Header -->
    <header class="mb-8">
      <h1 class="text-2xl font-bold text-gray-800">
        🎓 Student Dashboard
      </h1>
      <p class="text-gray-500">
        Welcome back, <span class="font-semibold">{{ user?.username }}</span>
      </p>
    </header>

    <!-- Loading / Error States -->
    <div v-if="loading" class="text-blue-500">Loading your info...</div>
    <div v-if="error" class="text-red-500">Failed to load data</div>

    <!-- Main Dashboard Content -->
    <div v-if="user" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <!-- Profile Card -->
      <div class="bg-white rounded-2xl shadow p-6">
        <h2 class="text-lg font-semibold mb-4">Profile</h2>
        <p><strong>Username:</strong> {{ user.username }}</p>
        <p><strong>Email:</strong> {{ user.email }}</p>
        <p><strong>Student ID:</strong> {{ user.studentID }}</p>
        <p><strong>Role:</strong> {{ user.role }}</p>
      </div>

      <!-- Exams Section -->
      <div class="bg-white rounded-2xl shadow p-6">
        <h2 class="text-lg font-semibold mb-4">Your Exams</h2>
        <ul class="list-disc list-inside text-gray-600">
          <li>Upcoming: Midterm Mathematics</li>
          <li>Upcoming: Computer Science Final</li>
          <li>Past: English Essay</li>
        </ul>
      </div>

      <!-- Notifications -->
      <div class="bg-white rounded-2xl shadow p-6">
        <h2 class="text-lg font-semibold mb-4">Notifications</h2>
        <p class="text-gray-600">✅ Registration complete</p>
        <p class="text-gray-600">📅 New exam schedule uploaded</p>
      </div>
    </div>
  </div>
</template>
