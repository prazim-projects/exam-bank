<script setup lang='ts'>
import navbar from './components/common/navbar'

</script>

<template>
  
    <div class="max-h-fit flex bg-blue-300 w-full h-15 text-2xl px-6 py-3"> <navbar /> </div>
    <main class="pt-6 mx-20 flex text-2xl font-mono text-amber-700">
    <NuxtPage />
    </main>
    <NuxtRouteAnnouncer />
    
</template>

<style lang="css">

.router-link-exact-active{
  text-size-adjust: 70px;
}


</style>
