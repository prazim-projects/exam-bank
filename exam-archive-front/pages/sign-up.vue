<script lang='ts' setup>

const CREATE_USER_MUTATION_STAFF = gql`
  mutation createUser($username: String!, $password: String!, $email: String!, $role: String!, $staffID: String! ){
    createUser(username: $username, password: $password, email: $email, role: $role, staffID: $staffID,){
      user{
        id
        email
        role
        username
        role
        staffID
      }    

    }
  }
`


const formData = ref({
  username: '',
  password: '',
  email: '',
  role: 'Student',
  studentID: '',
})

const fields = ref([
  { key: 'username', label: 'Username', type: 'text' },
  { key: 'password', label: 'Password', type: 'password' },
  { key: 'email', label: 'Email', type: 'email' },
  { key: 'studentID', label: 'studendID', type: 'text' },
])

 
const {mutate: createStaff, loading, onDone, error} = useMutation(CREATE_USER_MUTATION_STAFF)


onDone((result) => {
  if (result.data?.tokenAuth?.user) {
    
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
    await ({
      variables
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