<script setup lang='ts'>


const query = gql`
    query getExamPublic($visibility: String!, $limit: Int!, $offset: Int!){
      examByVisibility(visibility: $visibility, limit: $limit, offset: $offset){
          course {
            ExamCourses {
              code
              description
              id
              name}
            createdAt
            description
            id
            name
}

    }
  }`

const variables = {visibility: 'published', offset: 0, limit: 0}


// Define the expected structure for data
interface Exam {
  id: string
  title?: string
  year?: string
  difficultyratingSet?: Array<{ id: string; difficultyScore: number }>
  examFile?: Array<{ id: string; file: string }>
}

interface QueryResult {
  examByVisibility: Exam[]
}

const { data, loading, error } = await useAsyncQuery<QueryResult>(query, variables)

</script>

<template>
    <div class='container bg-vlue-100 mx-auto grid-col-3 text-xl text-black'>
      
      <h1>View Exams, Rate em, Get solutions!!</h1>
       
      <div v-if="loading">Loading...</div>
      <div v-else-if="error">Error: {{ error.message }}</div>
      <div v-else  class='bg-blend-color-burn '>
       <ul v-for="exam in data?.examByVisibility" :key="exam.id">
         <li>
           <span>{{ exam.title }}</span><br />
           <span>{{exam.year}}</span><br />
          <!-- <span>{{exam.}}</span><br /> -->
           <div v-for="score in exam.difficultyratingSet" :key="score.id">
            <span> difficulty rated: {{score.difficultyScore}} </span>
           </div>

           <div v-for="attr in exam.examFile" :key="attr.id">
             <a :href="`http://localhost:8000/media/${attr.file}`" target="blank"> {{attr.file}}</a>
           </div>
          </li>
        </ul>
        <div> <> Next page</div>
      </div>
  </div>
  </template>
  

<style lang='css'>


</style>