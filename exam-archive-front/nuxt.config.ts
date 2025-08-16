import { defineNuxtConfig } from "nuxt/config"
// https://nuxt.com/docs/api/configuration/nuxt-config


export default defineNuxtConfig({
  compatibilityDate: '2025-05-15',
  devtools: { enabled: true },
  modules: ['@nuxtjs/apollo', '@nuxt/ui', '@pinia/nuxt'],
  apollo: {
    autoImports: true,
    authType: 'Bearer',
    authHeader: 'Authorization',
    tokenStorage: 'cookie',
    proxyCookies: true,
    clients: {
      default: {
        httpEndpoint: 'http://localhost:8000/graphql'
      },
      other: 'apollo/other.ts'
    }
  },

  pinia: {
    storesDirs: ['./stores/**'],
  },
  css: ['~/assets/css/main.css'],
  ui: {
    prefix: 'Nuxt',
    fonts: false,
    colorMode: true,
    theme: {
      colors: ['primary', 'secondary', 'success', 'info', 'warning', 'error']
    }
  },

  apollo: {
    autoImports: true,
    authType: 'Bearer',
    authHeader: 'Authorization',
    tokenStorage: 'cookie',
    proxyCookies: true,
    clients: {      
      default: {       
        httpEndpoint: 'http://localhost:8000/graphql'  }    
    },  
  },
  pinia: {
    storesDirs: [ '/stores/**'],
  },
  debug: false,
})