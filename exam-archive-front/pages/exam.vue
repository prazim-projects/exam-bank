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

const { data, loading, error } = await useAsyncQuery(query)


</script>

<template>
    <div class='container bg-amber-100 mx-auto grid-col-3'>
      
      <h1>View Exams, Rate em, Get solutions!!</h1>
       
      <div v-if="loading">Loading...</div>
      <div v-else-if="error">Error: {{ error.message }}</div>
      <div v-else class='bg-blend-color-burn'>
       <ul v-for="exam in data?.allExams" :key="exam.id">
         <li>
           <span>{{ exam.title }}</span><br />
           <span>{{exam.year}}</span><br />
           <span>{{exam.course}}</span><br>
           <div v-for="score in exam.difficultyratingSet" :key="score.id">
            <span> difficulty rated: {{score.difficultyScore}} </span>
           </div>

           <div v-for="attr in exam.examFile" :key="attr.id">
             <embed :src="`http://localhost:8000/media/${attr.file}`">
           </div>
          </li>
        </ul>
      </div>
    <div>
    <examUpload />
    </div>
  </div>
  </template>
  

<style lang='css'>

div > embed{
  width: 200px;
  height: 200px;
}

</style>