<script>
    import { params } from "@roxi/routify";
    import MonthRatingChart from "../components/MonthRatingChart.svelte";
    import QualityIndex from "../components/QualityIndex.svelte";
    import TopFive from "../components/TopFive.svelte";
</script>

<main>
    <h1>{$params.city}, рейтинг качества</h1>
    <QualityIndex />
    <TopFive />
</main>

<style>
</style>

