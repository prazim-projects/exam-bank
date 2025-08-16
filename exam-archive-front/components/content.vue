<script setup lang='ts'>

const query = gql`
    query getExamPublic($visibility: String!, $limit: Int!, $offset: Int!){
      examByVisibility(visibility: $visibility, limit: $limit, offset: $offset){
          course
          department
          title
          year
          uploadDate
          examFile{
            file
            id
          }
          difficultyratingSet {
            difficultyScore
            id  
            ratedAt
            ratedBy {
              role
              staffID
              username
            }
          }

    }
  }`

const variables = {visibility: 'published', offset: 0, limit: 3}


const { data, loading, error } = await useAsyncQuery(query, variables)

</script>

<template>
    <div class='container bg-vlue-100 mx-auto grid-col-3 text-xl text-black'>
      
      <h1>View Exams, Rate em, Get solutions!!</h1>
       
      <div v-if="loading">Loading...</div>
      <div v-else-if="error">Error: {{ error.message }}</div>
      <div v-else class='bg-blend-color-burn '>
       <ul v-for="exam in data?.examByVisibility" :key="exam.id">
         <li>
           <span>{{ exam.title }}</span><br />
           <span>{{exam.year}}</span><br />
           <span>{{exam.course}}</span><br>
           <div v-for="score in exam.difficultyratingSet" :key="score.id">
            <span> difficulty rated: {{score.difficultyScore}} </span>
           </div>

           <div v-for="attr in exam.examFile" :key="attr.id">
             <a :href="`http://localhost:8000/media/${attr.file}`" target="blank"> {{attr.file}}</a>
           </div>
          </li>
        </ul>
        <div> <button @click="nextPage"> Next page</button></div>
      </div>
  </div>
  </template>
  

<style lang='css'>


</style>