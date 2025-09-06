<script setup lang='ts'>
// import { useAsyncQuery } from '@vue/apollo-composable'
const userStore  = useUserStore()

type Exam = {
  id: number
  title: string
  year: number
  difficultyratingSet: {difficultyScore: number, id:number}[]
  examFile: {file: string, id:number}[]
}

type ExamByVisibilityResult = {
  examByVisibility: Exam[]
}

type AllExamsResult = {
  allExams: Exam[]
}

const query = gql`
    query getExamPublic($visibility: String!, $limit: Int!, $offset: Int!){
      examByVisibility(visibility: $visibility, limit: $limit, offset: $offset){
        title
        id
        uploadDate
        year
        difficultyratingSet{
          difficultyScore
          id
        }
        examFile {
          file
          id
        }
      }
}`

const query_2 = gql `
  query getAllExams{
    allExams{
      id
      title
      year
      difficultyratingSet{
        difficultyScore
        id
      }
      examFile{
        file
        id
      }
    }
  }
`

const variables = { visibility: 'PUBLISHED', offset: 0, limit: 10}
const variables_1 = {offset: 0, limit: 4}
import { onMounted, watch } from 'vue'
import ExamCard from './exams/examCard.vue'


const { data, error } = await useAsyncQuery<ExamByVisibilityResult>(query, variables)
// const { data, error } = await useAsyncQuery<AllExamsResult>(query_2, variables_1)

// const { data, error } = await useAsyncQuery<AllExamsResult>(query_2, variables_1)

onMounted(() => {
  watch(
    () => data.value,
    (newData) => {
      console.log('Query response:', newData)
    },
    { immediate: true }
  )
})


</script>

<template>
    <div class='container bg-vlue-100 mx-auto grid-col-3 text-xl text-black'>
      
      <h1>View Exams, Rate em, Get solutions!!</h1>
      <div v-if="error">Error: {{ error.message }}</div>
      <div v-else class='bg-blend-color-burn '>
          <ExamCard 
            v-for="exam in data?.examByVisibility" 
            :key="exam.id" 
            :exam="exam" />
        </div>
      </div>
  </template>
  

<style lang='css'>


</style>