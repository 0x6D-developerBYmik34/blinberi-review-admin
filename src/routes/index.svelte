<script lang="ts">
    import { params } from "@roxi/routify";
    import MainPage from "../pages/MainPage.svelte";
    import CityPage from "../pages/CityPage.svelte";
</script>

{#if $params.city === undefined}
<MainPage />
{:else}
<CityPage />
{/if}
