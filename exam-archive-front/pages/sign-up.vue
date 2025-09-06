<script lang='ts' setup>

const userStore = useUserStore()
const routeTo = useRouter()

const CREATE_USER_MUTATION_STAFF = gql`
  mutation createUser($username: String!, $password: String!, $email: String!, $role: String!, $studentID: String) {
    createUser(username: $username, password: $password, email: $email, role: $role, studentID: $studentID) {
      token
      refreshToken
      user{
        id
        email
        role
        username
        role
        studentID
      }    

    }
  }
`

type formType = {
  username: string,
  password: string,
  email: string,
  role: string,
  studentID: string,
  [key: string]: string
}

const formData = ref<formType>({
  username: '',
  password: '',
  email: '',
  role: 'Student',
  studentID: '',
})

type fieldType = {
  key: string,
  label: string,
  type: string
}

const fields = ref<fieldType[]>([
  { key: 'username', label: 'Username', type: 'text' },
  { key: 'password', label: 'Password', type: 'password' },
  { key: 'email', label: 'Email', type: 'email' },
  { key: 'studentID', label: 'studentID', type: 'text' },
])

 
const {mutate: createStaff, loading, onDone, error} = useMutation(CREATE_USER_MUTATION_STAFF)


onDone((result) => {
  if (result.data?.createUser.token) {
    console.log('User created successfully:', result.data.createUser.user)
    const user = result.data.createUser
    userStore.setUser(user.user)
    userStore.setToken(user.token, user.refreshToken)
     
    if (userStore.getUser?.role==='DEPARTMENT' ){
      routeTo.push(`/department/`)
    }
    else if(userStore.getUser?.role==='COLLEGE'){
      routeTo.push('/univ/')
    }
    else if(userStore.getUser?.role==='STUDENT'){
      routeTo.push(`/students/`)
      
    }
  }


})


const onSubmit = async () => {
  try {
    const variables = {
      username: formData.value.username,
      password: formData.value.password
    }
    await createStaff({
      username: formData.value.username,
      password: formData.value.password,
      email: formData.value.email,
      role: formData.value.role,
      studentID: formData.value.studentID,
    })
  } catch (err) {
    console.error(err)
  }
}

</script>

<template>
<div class="max-w-lg mx-auto mt-10 bg-white rounded-xl shadow-lg p-6">
    <h2 class="text-2xl font-bold mb-6 text-center">Register User</h2>

    <form @submit.prevent="onSubmit" class="space-y-4">
      <div v-for="field in fields" :key="field.key">
        <label :for="field.key" class="block font-medium mb-1">{{ field.label }}</label>
        <input
          :id="field.key"
          v-model.trim="formData[field.key]"
          :type="field.type"
          class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring focus:border-blue-500"
          required
        />
      </div>
      <button
        type="submit"
        :disabled="loading"
        class="w-full bg-blue-600 text-white font-medium py-2 px-4 rounded-lg hover:bg-blue-700 transition-colors disabled:opacity-50"
      >
        {{ loading ? 'Registering...' : 'Register' }}
      </button>

      <!-- Error message -->
      <p v-if="error" class="text-red-600 text-sm mt-2">
        {{ error.message }}
      </p>
    </form>
  </div>
</template>

<style scoped>


</style>