<script setup lang="ts">

const route = useRoute()
const pages = [
    { name: 'Home', path: '/'},
    { name: 'Exams', path: '/exam'},
    {name: 'sigin/Login', path: '/sign-in'}
]

function isActive(path) {
  return route.path === path
}

</script>

<template>
    <div class='navbar fixed top-0 left-0 w-full z-50 shadow h-16' >
        <div class='mx-auto'>
            <nav class="flex"> 
                <ul>
               <div class='grid grid-cols-3'>
                <li v-for='(page, index) in pages' :key="index"> 
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
                </li></div>
            </ul>
        </nav>
    </div>
    </div>
</template>

<style>
</style>