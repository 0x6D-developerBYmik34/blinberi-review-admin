
<script lang="ts">
    import { params } from "@roxi/routify";
    import MonthRatingChart from "../components/MonthRatingChart.svelte";
    import QualityIndex from "../components/QualityIndex.svelte";
    import TopFive from "../components/TopFive.svelte";
    import LocationRatingList from "../components/LocationRatingList.svelte";
    import CityRatingList from "../components/CityRatingList.svelte";


    function brandIDToName(id: string): string {
        const dict: any = {
           "1": "Блинберри",
           "2": "СушиВёсла",
        }
        return dict?.[id];
    }

    $: brandName = brandIDToName($params['brand-id'])

</script>

<main> 
    {#if brandName}
    <h1>{brandName}, рейтинг качества</h1>
    <QualityIndex />
    <TopFive />
    <!-- <MonthRatingChart /> -->
    <LocationRatingList />
    <CityRatingList />
    {:else}
    <h1>Страница не найдена!</h1>
    {/if}
</main>
