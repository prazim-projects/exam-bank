import { defineNuxtPlugin, useCookie } from '#app'
import {
  ApolloClient,
  InMemoryCache,
  createHttpLink,
  ApolloLink,
  fromPromise,
} from '@apollo/client/core'
import { onError } from '@apollo/client/link/error'
import { useUserStore } from '@/stores/user.store'

export default defineNuxtPlugin((nuxtApp) => {
  const httpLink = createHttpLink({
    uri: 'http://localhost:8000/graphql/', // same as nuxt.config.ts
  })

    const userStore = useUserStore()
  // 🔑 Attach Authorization header
  const authLink = new ApolloLink((operation, forward) => {
    const token = userStore.jw_token
    // const token = useCookie<string | null>('jwt').value
    operation.setContext(({ headers = {} }) => ({
      headers: {
        ...headers,
        authorization: token ? `Bearer ${token}` : "",
      },
    }))
    return forward(operation)
  })

  // 🔄 Handle expired tokens
  const errorLink = onError(({ graphQLErrors, operation, forward }) => {
    const tokenCookie = useCookie<string | null>('jwt')
    const refreshCookie = useCookie<string | null>('refresh')

    if (graphQLErrors) {
      for (const err of graphQLErrors) {
        if (err.message.includes('Signature has expired')) {
          // try refreshing token
          return fromPromise(
            fetch('http://localhost:8000/graphql/', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({
                query: `
                  mutation RefreshToken($refreshToken: String!) {
                    refreshToken(refreshToken: $refreshToken) {
                      token
                      payload
                    }
                  }
                `,
                variables: { refreshToken: refreshCookie.value },
              }),
            })
              .then((res) => res.json())
              .then((res) => {
                const newToken = res?.data?.refreshToken?.token
                if (newToken) {
                  tokenCookie.value = newToken
                  return newToken
                }
                return null
              })
          )
            .filter((newToken) => Boolean(newToken))
            .flatMap((newToken) => {
              if (!newToken) return forward(operation)

              // Retry failed operation with new token
              operation.setContext(({ headers = {} }) => ({
                headers: {
                  ...headers,
                  Authorization: `Bearer ${newToken}`,
                },
              }))
              return forward(operation)
            })
        }
      }
    }
  })

  const apolloClient = new ApolloClient({
    link: ApolloLink.from([errorLink, authLink, httpLink]),
    cache: new InMemoryCache(),
  })

  // Provide client to Nuxt
  nuxtApp.provide('apollo', apolloClient)
})
