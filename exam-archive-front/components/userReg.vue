<script setup>
import { ref, reactive, computed } from 'vue'

const form = reactive({
  username: '',
  email: '',
  password: '',
  role: '',
  file: null,
  StaffID: '',
  studentId: '',
  department: '',

})

const showStudentFields = computed(() => form.role === 'student')
const showInstructorFields = computed(() => form.role === 'instructor')

function handleFileUpload(e) {
  form.file = e.target.files[0]
}

function submitForm() {
  console.log({ ...form })}
</script>

<template>
  <form @submit.prevent="handleRegistration" class="p-4 space-y-4 max-w-md mx-auto border rounded bg-amber-100">
    <input v-model="form.username" type="text" placeholder="Username" class="w-full p-2 border rounded" />
    <input v-model="form.email" type="email" placeholder="Email" class="w-full p-2 border rounded" />
    
    <select v-model="form.role" class="w-full p-2 border rounded">
      <option disabled value="">Select Role</option>
      <option value="student">Student</option>
      <option value="instructor">Instructor</option>
    </select>

    <input v-model="form.password" type="password" placeholder="Password" class="w-full p-2 border rounded" />
    
    <div v-if="showStudentFields" class="space-y-2">
      <input v-model="form.studentId" type="text" placeholder="Student ID" class="w-full p-2 border rounded" />
      <input v-model="form.department" type="text" placeholder="Department" class="w-full p-2 border rounded" />
    </div>

    <div v-if="showInstructorFields" class="space-y-2">
      <input v-model="form.department" type="text" placeholder="Department" class="w-full p-2 border rounded" />
      <input v-model="form.StaffID" type="text" placeholder="StaffID" class="w-full p-2 border rounded" />
    </div>

    <button type="submit" class="w-full bg-black text-white py-2 rounded">Submit</button>
  </form>
</template>