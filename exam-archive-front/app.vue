<script setup lang='ts'>

</script>

<template>
  <UApp> 
    <navbar />
    <NuxtPage />
    <NuxtRouteAnnouncer />
  </UApp>
</template>

<style lang="css">

nav{
  
  width: 100%;
  background-color: rgb(11, 85, 80);
}

ul {
  display: flex;
  flex-direction: row;

}
nav > ul > li {
  width: 70px;
  margin: 20px;
  height: 20px;
  
}

.router-link-exact-active{
  text-size-adjust: 70px;
}


</style>
