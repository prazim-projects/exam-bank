<script setup lang="ts">
import { ref } from 'vue'
import { useMutation } from '@vue/apollo-composable'
import gql from 'graphql-tag'
import {useUserStore} from '../stores/user.store'
import { ro } from '@nuxt/ui/runtime/locale/index.js'

// Reactive state for login form
const username = ref('')
const password = ref('')
const role = ref<String | null>(null)

const userStore = useUserStore()
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
        studentID
        email
      }
    }
  }
`

const { mutate: login, loading, error, onDone } = useMutation(TOKEN_AUTH_MUTATION)


// When mutation finishes successfully
onDone((result) => {
  if (result.data?.tokenAuth?.token) {
    userStore.setToken(result.data.tokenAuth.token,result.data.tokenAuth.refreshToken )
    userStore.setUser(result.data.tokenAuth.user)

    if (userStore.getUser?.role==='DEPARTMENT' ){
      route.push(`/department/`)
    }
    else if(userStore.getUser?.role==='College'){
      route.push('/univ/')
    }
    else if(userStore.getUser?.role==='STUDENT'){
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
    <!-- <div v-if="authToken"><NuxtLink to=""> </NuxtLink></div> -->
  </div>
</template>
