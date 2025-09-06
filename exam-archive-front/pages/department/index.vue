<script setup lang="ts">
import { useQuery } from "@vue/apollo-composable"
import gql from "graphql-tag"
import { ref, watch } from "vue"
import { useUserStore } from "@/stores/user.store"

// Store: contains logged-in user info
const userStore = useUserStore()

// GraphQL query: fetch staff details
const GET_USER = gql`
  query GetUser($id: String!) {
    userById(id: $id) {
      id
      username
      email
      role
    }
  }
`

const { result, loading, error } = useQuery(GET_USER, {
  id: userStore.loggedUser?.id
})

const staff = ref(null)

watch(result, (val) => {
  if (val?.userById) {
    staff.value = val.userById
  }
})
</script>

<template>
  <div class="min-h-screen bg-gray-100 p-6">
    <!-- Header -->
    <header class="mb-8">
      <h1 class="text-2xl font-bold text-gray-800">
        🧑‍🏫 Staff Dashboard
      </h1>
      <p class="text-gray-500">
        Welcome back, <span class="font-semibold">{{ userStore.loggedUser?.username }}</span>
      </p>
    </header>

    <!-- Loading / Error States -->
    <div v-if="loading" class="text-blue-500">Loading your data...</div>
    <div v-if="error" class="text-red-500">Failed to fetch staff details</div>

    <!-- Dashboard Content -->
    <div v-if="staff" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <!-- Profile Card -->
      <div class="bg-white rounded-2xl shadow p-6">
        <h2 class="text-lg font-semibold mb-4">Profile</h2>
        <p><strong>Name:</strong> {{ userStore.loggedUser?.username }}</p>
        <p><strong>Email:</strong> {{ userStore.loggedUser?.email }}</p>
        <p><strong>Role:</strong> {{ userStore.loggedUser?.role }}</p>
      </div>

      <!-- Manage Exams -->
      <div class="bg-white rounded-2xl shadow p-6">
        <h2 class="text-lg font-semibold mb-4">Manage Exams</h2>
        <ul class="space-y-2 text-gray-600">
          <li>➕ Create New Exam</li>
          <li>📄 View All Exams</li>
          <li>✏️ Edit Existing Exams</li>
        </ul>
      </div>

      <!-- Student Management -->
      <div class="bg-white rounded-2xl shadow p-6">
        <h2 class="text-lg font-semibold mb-4">Students</h2>
        <ul class="space-y-2 text-gray-600">
          <li>👨‍🎓 View Registered Students</li>
          <li>📊 Student Performance Reports</li>
        </ul>
      </div>

      <!-- Notifications -->
      <div class="bg-white rounded-2xl shadow p-6 col-span-1 md:col-span-2">
        <h2 class="text-lg font-semibold mb-4">Notifications</h2>
        <p class="text-gray-600">📢 New exam requests pending approval</p>
        <p class="text-gray-600">✅ System update completed</p>
      </div>
    </div>
  </div>
</template>
