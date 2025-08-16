<script setup lang="ts">

const route = useRoute()
const pages = [
    { name: 'Home', path: '/'},
    { name: 'Exams', path: '/exam/exam'},
    {name: 'Register', path: '/sign-up'},
    {name: 'Login', path: '/login'},
]

function isActive(path) {
  return route.path === path
}

</script>

<template>
    <nav class="flex navbar navbar-expand-lg fixed-top text-black"> 
            <a class="navbar-brand logo-text"> ETDU eXAM BANK</a>
            
            <div class="navar-collapse">
                <ul class='flex flex-row'>
                <li v-for='(page, index) in pages' :key="index" class="px-5"> 
                   <NuxtLink  
                   :to="page.path"
                   :class="[
                    'px-3 py-2 rounded transition-colors duration-200',
                    isActive(page.path)
                    ? 'bg-black text-white'
                    : 'text-black hover:bg-black hover:text-white']"
                   > 
                   {{ page.name }}
                    </NuxtLink>
                    </li>
                </ul>
            </div>
    </nav>
</template>

<style>
</style>