import { ApolloClient, InMemoryCache } from '@apollo/client';
import { defineNuxtPlugin } from '#app';

export default defineNuxtPlugin((nuxtApp) => {
  const apolloClient = new ApolloClient({
    uri: 'https://localhost:8000/graphql',
    cache: new InMemoryCache(),
  });

  nuxtApp.vueApp.provide('apollo', { default: apolloClient });
});