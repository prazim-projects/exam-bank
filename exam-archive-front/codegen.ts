import type { CodegenConfig } from '@graphql-codegen/cli'
 
const config: CodegenConfig = {
   schema: 'http://localhost:8000/graphql',
   documents: ['src/**/*.tsx'],
   generates: {
      './src/_generated_/': {
        preset: 'client',
        presetConfig: {
            gqlTagName: "gql",
        } 
      },
      "./src/_generated_/types.ts": {
        plugins: ["typescript", "typescript-operations"],
      },
   },
   ignoreNoDocuments: true
}
export default config