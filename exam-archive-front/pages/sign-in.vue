<script setup lang="ts">

const CREATE_USER_MUTATION = gql`
  mutation createUser($user: userInput!){
    createUser(user: $user){
      id
      role
      username
    }
  }
`
const TOKEN_AUTH_MUTATION = gql`
  mutation tokenAuth($username: String!, $password: String!){
    tokenAuth(username: $username, password: $password){
      token
      payload
      refreshExpiresIn
    }
  }
`

interface userInput {
  name: string
  email: string
  password: string
  role: string
  department: string
  studentID?: string
  staffID?: string
}




const username = ref<string>('')
const email = ref<string>('')
const password = ref<string>('')
const role = ref<string>('')
const department = ref<string>('')
const staffID = ref<string>('')
const studentID = ref<string>('')

const {mutate, loading, error, onDone } = await useMutation(CREATE_USER_MUTATION, ()=>({
  variables: {
    user: userInput.value
  }
})) 
</script>

<template>
<form @submit.prevent="createUser" class="bg-amber-950">
    <input v-model="username" type="text" placeholder="Username" required />
    <input v-model="email" type="email" placeholder="Email" required />
    <input v-model="password" type="password" placeholder="Password" required />
    <input v-model="department" type="text" placeholder="Department" required />
    <select v-model="role" required>
      <option value="" disabled>Select Role</option>
      <option value="student">Student</option>
      <option value="teacher">Teacher</option>
    </select>
    <input
      v-if="role === 'student'"
      v-model="studentId"
      type="text"
      placeholder="Student ID"
      required
    />
    <input
      v-if="role === 'teacher'"
      v-model="department"
      type="text"
      placeholder="Department"
      required
    />
    <button type="submit" :disabled="createLoading || authLoading">Register</button>
    <p v-if="createError">{{ createError.message }}</p>
    <p v-if="authError">{{ authError.message }}</p>
  </form>
</template>