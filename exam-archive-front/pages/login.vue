<script setup lang="ts">
import { ref } from 'vue'
import { useMutation } from '@vue/apollo-composable'
import gql from 'graphql-tag'

// Reactive state for login form
const username = ref('')
const password = ref('')
const role = ref<String | null>(null)
const authToken = ref<string | null>(null) // Store JWT token
const token = useCookie('jwt')
const route = useRouter()

// GraphQL login mutation
const TOKEN_AUTH_MUTATION = gql`
  mutation tokenAuth($username: String!, $password: String!) {
    tokenAuth(username: $username, password: $password) {
      token
      payload
      refreshExpiresIn
      user {
        id
        role
        username
      }
    }
  }
`

// Apollo mutation hook
const { mutate: login, loading, error, onDone } = useMutation(TOKEN_AUTH_MUTATION)


// When mutation finishes successfully
onDone((result) => {
  if (result.data?.tokenAuth?.token) {
    authToken.value = result.data.tokenAuth.token
    token.value = authToken.value
    // localStorage.setItem('jwt', authToken.value)
    console.log('Login successful! Token saved.')
    role.value = result.data.tokenAuth.user.role
    console.log(`ROLE: ${role.value}`  )
    if (role.value==='STAFF'){
      route.push(`/department/`)
    }
    else if(role.value==='student'){
      route.push(`/students/`)
    }
  }
})

// Login function
const loginAuth = async () => {
  if (!username.value || !password.value) {
    console.warn('Username and password are required')
    return
  }

  try {
    await login({
      username: username.value,
      password: password.value
    })
  } catch (err) {
    console.error('Login failed:', err)
  }
}
</script>

<template>
  <div>
    <input v-model="username" placeholder="Username" />
    <input v-model="password" type="password" placeholder="Password" />
    <button @click="loginAuth" :disabled="loading">Login</button>

    <div v-if="loading">Logging in...</div>
    <div v-if="error">Error: {{ error.message }}</div>
    <div v-if="authToken"><NuxtLink to=""> </NuxtLink></div>
  </div>
</template>
