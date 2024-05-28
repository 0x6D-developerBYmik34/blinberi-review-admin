<script>
    import { params } from "@roxi/routify";
    import BrandCityPage from "../../pages/BrandCityPage/BrandCityPage.svelte";
    import BrandPage from "../../pages/BrandPage/BrandPage.svelte";
</script>
{#if $params.city !== undefined}
<BrandCityPage/>
{:else}
<BrandPage />
{/if}
