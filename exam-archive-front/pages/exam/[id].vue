<script setup>

const route = useRoute()

// GraphQL Query for a single exam
const GET_EXAM = gql`
query getExam($id: ID!) {
  exam(id: $id) {
    id
    title
    description
    createdAt
    privacy
  }
}`

const { result, loading, error } = useQuery(GET_EXAM, {
  id: route.params.id
})
</script>

<template>
  <div class="p-6">
    <div v-if="loading">Loading exam...</div>
    <div v-if="error">{{ error.message }}</div>

    <div v-if="result?.exam" class="bg-white p-6 rounded-lg shadow-md">
      <h1 class="text-2xl font-bold">{{ result.exam.title }}</h1>
      <p class="mt-2 text-gray-600">{{ result.exam.description }}</p>
      <p class="mt-4 text-sm text-gray-500">Created: {{ result.exam.createdAt }}</p>
      <p class="mt-1 text-sm" :class="result.exam.privacy === 'PRIVATE' ? 'text-red-600' : 'text-green-600'">
        Privacy: {{ result.exam.privacy }}
      </p>
    </div>
  </div>
</template>
