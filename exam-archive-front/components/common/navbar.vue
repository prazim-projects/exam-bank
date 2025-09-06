<script setup lang="ts">

const route = useRoute()
const userStore = useUserStore()

const authStatus = userStore.isAuthenticated

const pages = [
    { name: 'Home', path: '/'},
    { name: 'Exams', path: '/exam/exam'},

]

function isActive(path: string): boolean {
  return route.path === path
}

const authTabs = computed(()=> {
    if(userStore.getUser?.role === 'DEPARTMENT'){
        return {
            ...pages.concat({name: 'StaffHome', path: '/department/'}, {name: 'uploadExam', path: '/department/upload'}, {name: 'logout', path: '/logout'})
        }
    }
    else if(userStore.getUser?.role === 'STUDENT'){
        return {
            ...pages.concat(
                { name: 'StudentHome', path: '/students/' },
                { name: 'logout', path: '/logout' }
            )
        }
    }
    else {
        return {
            ...pages.concat({name: 'Register', path: '/sign-up'}, {name: 'Login', path: '/login'},
)

        }
    }
})

</script>

<template>
    <nav class="flex navbar navbar-expand-lg fixed-top text-black"> 
            <a class="navbar-brand logo-text"> ETDU eXAM BANK</a>
            
            <div class="navar-collapse">
                <ul class='flex flex-row'>
                <li v-for='(page, index) in authTabs' :key="index" class="px-5"> 
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