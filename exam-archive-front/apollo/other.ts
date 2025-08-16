import { defineApolloClient } from '@nuxtjs/apollo/config'

export default defineApolloClient({
  httpEndpoint: 'http://localhost:8000/graphql',
  browserHttpEndpoint: '',
  httpLinkOptions: {},
  websocketsOnly: false,
  connectToDevTools: false,
  defaultOptions: {},
  inMemoryCacheOptions: {},
  tokenName: 'apollo:<client-name>.token',
  tokenStorage: 'cookie',
  authType: 'Bearer',
  authHeader: 'Authorization'
})
