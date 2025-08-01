<template>
  <form @submit.prevent="submitForm">

    <input v-model="title" type="text" placeholder="Exam Title" required />
    <input type="file" @change="handleFileChange" required />
    <button type="submit">Upload</button>
  </form>
</template>

<script setup>
import { useMutation } from '@vue/apollo-composable'
import gql from 'graphql-tag'
import { ref } from 'vue'

const title = ref('')
const file = ref(null)

const CREATE_EXAM_WITH_FILE = gql`
  mutation CreateExamWithFile($examTitle: String!, $file: Upload!) {
    createExamWithFile(examTitle: $examTitle, file: $file) {
      exam {
        id
        title
      }
      examFile {
        id
        fileName
      }
    }
  }
`

const { mutate } = useMutation(CREATE_EXAM_WITH_FILE)

function handleFileChange(event) {
  file.value = event.target.files[0]
}

async function submitForm() {
  try {
    const { data } = await mutate({
      examTitle: title.value,
      file: file.value,
    })
    console.log('Success:', data)
  } catch (error) {
    console.error('Upload failed:', error)
  }
}
</script>
