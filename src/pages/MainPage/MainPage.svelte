<script lang="ts">
    import '../style.css'
    import MonthRatingChart from "../../components/MonthRatingChart.svelte";
    import TopFiveLocations from "../../components/TopFiveLocations.svelte";
    import QualityIndexWithLoad from "../../components/QualityIndexWithLoad.svelte";
    import Card from '@smui/card'
    const filterProp ={
        city: undefined,
        brand: undefined
    }
</script>

<main>
    <h1>Сервис рейтинга качества</h1>
    <article class="info-container">
        <div class="qi"><QualityIndexWithLoad filterProp={filterProp} /></div>
        <div class="tf"><TopFiveLocations filterProp={filterProp}/></div>
    </article>
    <div class="mchr">
        <Card variant="outlined" padded>
            <MonthRatingChart filterProp={filterProp}/>
        </Card>
    </div>
</main>
