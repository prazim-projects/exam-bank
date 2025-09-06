<script setup lang="ts">
import { useUserStore } from '#imports'

const userStore = useUserStore()

onMounted(() => {
    userStore.clearAuth()
    useRouter().replace('/login')
})
</script>
<template>
    <div class="logout-page">
        <p>Logging out...</p>
    </div>
</template>