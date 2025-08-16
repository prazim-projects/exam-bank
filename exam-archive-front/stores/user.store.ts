import {defineStore} from 'pinia'

export const useUserStore = defineStore('auth', ()=> {

    const loggedUser = ref("")
    const isLoggedIn = computed(() => !!loggedUser.value)
    
    const getToken = localStorage.getItem('token') as '' || localStorage.getItem('jwt')
    const getRole = localStorage.getItem('role') as '' || localStorage.getItem('role')
    const getUsername = localStorage.getItem('uname') as '' || localStorage.getItem('uname')



}
)

