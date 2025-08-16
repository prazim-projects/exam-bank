import { defineNuxtPlugin } from '#app';
import { createPersistedState } from 'pinia-plugin-persistedstate';

export default defineNuxtPlugin((nuxtApp) => {
    nuxtApp.$pinia.use(createPersistedState({
        storage: {
            getItem: (key) => {
                if (process.client) {
                    return cookie.parse(document.cookie)[key];
                }
                // For SSR, you'd need to access cookies from the server request
                // This often involves Nuxt's useRequestHeaders or similar
            },
            setItem: (key, value) => {
                if (process.client) {
                    document.cookie = cookie.serialize(key, value);
                }
                // For SSR, you'd need to set cookies on the server response
            },
            removeItem: (key) => {
                if (process.client) {
                    document.cookie = cookie.serialize(key, '', { expires: new Date(0) });
                }
                // For SSR, similar to setItem
            },
        },
    }));
});