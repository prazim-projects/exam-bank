<script setup lang="ts">

const route = useRoute()
const pages = [
    { name: 'Home', path: '/'},
    { name: 'Exams', path: '/exam'}
]

function isActive(path) {
  return route.path === path
}

</script>

<template>
    <div class='navbar' >
        <nav> 
            <ul  class="flex gap-4">
               <li v-for='(page, index) in pages' :key="index"> 
                   <NuxtLink  
                   :to="page.path"
                   :class="[
                 'px-3 py-2 rounded transition-colors duration-200',
                isActive(page.path)
                ? 'bg-black text-white'
                : 'text-black hover:bg-black hover:text-white'
            ]"
                   > 
                   {{ page.name }}</NuxtLink>
                </li>
            </ul>
        </nav>
    </div>
</template>

<style>
</style>