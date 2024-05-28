<script lang="ts">
    import { params } from "@roxi/routify";
    import MainPage from "../pages/MainPage/MainPage.svelte";
    import CityPage from "../pages/CityPage/CityPage.svelte";
</script>

{#if $params.city !== undefined}
<CityPage />
{:else}
<MainPage />
{/if}
