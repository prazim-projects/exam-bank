<script setup lang="ts">

const form = reactive({
  file: null,
  StaffID: '',
  course: '',

})

const showStudentFields = computed(() => form.role === 'student')
const showInstructorFields = computed(() => form.role === 'instructor')

function handleFileUpload(e) {
  form.file = e.target.files[0]
}

function submitForm() {
  console.log({ ...form })}



  const mutation = gql`
  mutation uploadExam($file: file!){
    uploadExam (file: $file) {
      success
    }
  }
`


</script>

<template>
  
  <form @submit.prevent="submitForm" class="p-4 space-y-4 max-w-md mx-auto border rounded bg-amber-100">
    
       
    <input type="file" @change="handleFileUpload" class="w-full" />

    
    <div class="space-y-2">
      <input v-model="form.course" type="text" placeholder="Course" class="w-full p-2 border rounded" />
      <input v-model="form.StaffID" type="text" placeholder="StaffID" class="w-full p-2 border rounded" />
    </div>

    <button type="submit" class="w-full bg-black text-white py-2 rounded">Submit</button>
  </form>
</template>
