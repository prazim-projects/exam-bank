<script setup lang='ts'>

const query = gql`
    query getExams{
        allExams{
            course
            department
            title
            year
            uploadDate
            examFile{
              file
              id
            }
        }
    }`
    
const { data, loading, error } = await useAsyncQuery(query)

</script>

<template>
    <div>
      <h1>View Exams, Rate em, Get solutions!!</h1>
  
      <div v-if="loading">Loading...</div>
      <div v-else-if="error">Error: {{ error.message }}</div>
      <div v-else>
      <ul v-for="exam in data?.allExams" :key="exam.id">
        <li>
          <span>{{ exam.title }}</span><br />
          <span>{{exam.year}}</span><br />
          <span>{{exam.course}}</span><br>
          <div v-for="attr in exam.examFile" :key="attr.id">
            <span>{{ attr.file }}</span>
          </div>
        </li>
      </ul>
    </div>
    </div>
  </template>
  

<style lang='css'>


</style>