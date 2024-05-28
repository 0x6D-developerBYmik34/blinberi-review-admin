<script lang="ts">
  import { Router, createRouter } from "@roxi/routify";
  import routes from '../.routify/routes.default.js'
    import { setContext } from "svelte";
  
  export const router = createRouter({routes});
 
  // setContext('viewmanager', new BRAViewManager())
</script>

<Router {router}/>
