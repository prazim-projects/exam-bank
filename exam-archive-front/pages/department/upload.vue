<template>
  <div>
    <h1>Create New Exam</h1>
    <form @submit.prevent="submitExam">
     <div>
        <label for="title">Title:</label>
        <select id="title" v-model="formState.title" required>
          <option value="Final">FINAL</option>
          <option value="Mid">MID</option>
          <option value="Quiz">QUIZ</option>
        </select>
      </div>
      <div>
        <label for="course">Course:</label>
        <input id="course" v-model="formState.course" type="text" required />
      </div>
      <div>
        <label for="year">Year:</label>
        <input id="year" v-model.number="formState.year" type="number" required />
      </div>
      <div>
        <label for="visibility">Visibility:</label>
        <select id="visibility" v-model="formState.visibility" required>
          <option value="Published">Public</option>
          <option value="Draft">Private</option>
          <option value="Archived">Archived</option>
        </select>
      </div>
      <div>
        <label for="file">Exam File:</label>
        <!-- Use a ref to get the file object -->
        <input id="file" type="file" @change="handleFileChange" required />
      </div>

      <!-- Disable button while loading -->
      <button type="submit" :disabled="loading">
        {{ loading ? 'Uploading...' : 'Create Exam' }}
      </button>

      <!-- Display feedback to the user -->
      <p v-if="error" class="error">An error occurred: {{ error.message }}</p>
      <p v-if="uploadSuccess" class="success">Exam created successfully!</p>
    </form>
  </div>
</template>

<script lang="ts" setup>

const userStore = useUserStore()

const formState = reactive({
  title: '',
  course: '',
  uploadedBy: '',
  year: new Date().getFullYear(),
  visibility: '',
})

// Use a ref for the file, as it's not a simple value
const examFile = ref<File | null>(null)
const uploadSuccess = ref(false)
const CREATE_EXAM = gql`mutation CreateExam($course: String!, $title: String!, $uploadedBy: String!, $year: Int!, $visibility: String!, $file: Upload!) {
  createExam(
    course: $course
    title: $title
    uploadedBy: $uploadedBy
    year: $year
    visibility: $visibility
    file: $file
  ) {
    examFile {
      id
      file
    }
  }
}
`

const GET_COURSES = gql`
  query MyQuery {
    ExamCourses {
      code
      id
      slug
      description
  }
}`


const { data: courseData } = await useAsyncQuery(GET_COURSES)
// Pass the gql document to the composable
const { mutate, loading, error, onDone } = useMutation(CREATE_EXAM)


// This function captures the File object from the input
function handleFileChange(event: Event) {
  const target = event.target as HTMLInputElement
  if (target.files && target.files.length > 0) {
    examFile.value = target.files[0]
  }
}

onDone((result) => {
  console.log('Mutation successful:', result.data)
  uploadSuccess.value = true
  // Optionally reset the form or redirect the user
  useRouter().push('/exam/exam')
})


async function submitExam() {
  uploadSuccess.value = false

  // Guard clause to ensure a file was selected
  if (!examFile.value) {
    alert('Please select a file to upload.')
    return
  }
  
  // Call the 'mutate' function with the variables
  await mutate({
    ...formState,
    uploadedBy: userStore.getUser?.id,
    file: examFile.value,
  })
}
</script>

<style scoped>
.error {
  color: red;
}
.success {
  color: green;
}
</style>