import {defineStore} from 'pinia'
import apolloClient from '~/plugins/apollo-client'
import piniaPersistedstate from '~/plugins/pinia-persistedstate'

export const useUserStore = defineStore('auth', ()=> {
    // type definition
    type user = {
        email: string,
        id : string,
        role: string,
        studentID: string,
        username: string
    }

    // State
    const loggedUser = ref<user | null>(null)
    const role = useCookie('role')
    const jw_token = useCookie('jwt')
    const refresh_token = useCookie('refresh_token')

    // function sendAuthHeader(){
        
    // }
    function setUser(userData: user) {
        loggedUser.value = userData
        role.value = userData.role
        localStorage.setItem('uname', userData.username)
        localStorage.setItem('studentID', userData.studentID || '')
    }

    function setToken(token:string, ref_token: string){
        jw_token.value = token
        refresh_token.value = ref_token
    }

    function clearAuth() {
        loggedUser.value = null
        role.value = null
        jw_token.value = null
        role.value = null
        localStorage.removeItem('uname')
        localStorage.removeItem('studentID')
    }

    // Getters
    const getToken = computed(()=> jw_token.value)
    const isAuthenticated = computed(()=> !!jw_token.value)
    const getUser = computed(()=> loggedUser.value)
    const getRefreshToken = computed(()=> refresh_token.value)

    return { loggedUser, role, jw_token, setUser, clearAuth, setToken, getToken, isAuthenticated, getUser }

}, {
    persist: {
        storage: piniaPluginPersistedstate.cookies(),
    }
}
)

