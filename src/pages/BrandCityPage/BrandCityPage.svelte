<script lang="ts">
    import '../style.css'
    import Card from '@smui/card'
    import { params } from "@roxi/routify";
    import MonthRatingChart from "../../components/MonthRatingChart.svelte";
    import RatingListWithFilter from "../../components/RatingListWithFilter.svelte";
    import { BrandCityPageViewManager } from "./BrandCityPageViewManager";
    import QualityIndexWithLoad from "../../components/QualityIndexWithLoad.svelte";
    import TopFiveLocations from "../../components/TopFiveLocations.svelte";

    const viewmanager = new BrandCityPageViewManager(
        $params['brand'], $params.city
    )
    const filterProp = {
        brand: $params['brand'], 
        city: $params.city
    }

    const locationProps = viewmanager.brandCityProps 
    $: ({brand, city} = $locationProps)

    let locationRatingStrips: ReviewStripIf[] = []
    viewmanager.locationRatingList.subscribe(
        arr => {
            locationRatingStrips = arr.map(
                obj => ({
                    index: obj.rating,
                    localHead: obj.name,
                    localDescription: obj.addrs,
                    amountDescriptuion: obj.amount_reviews + ' Отзывов'
                })
            )
        }
    )

</script>

<main> 
    {#await viewmanager.loadData()}
    <h1>Загрузка...</h1>
    {:then res_ok} 
    <h1>{brand}, {city}, рейтинг каечтва</h1>
    <article class="info-container">
        <div class="qi"><QualityIndexWithLoad filterProp={filterProp} /></div>
        <div class="tf"><TopFiveLocations filterProp={filterProp}/></div>
    </article>
    <div class="mchr">
        <Card variant="outlined" padded>
            <MonthRatingChart filterProp={filterProp}/>
        </Card>
    </div>
    <RatingListWithFilter objList={locationRatingStrips} onChangeFilterValue={()=>{}}>
        Рейтинг
    </RatingListWithFilter> 
    {:catch error}
    <h1>Ошибка!</h1>
    <p>{error}</p>
    {/await}  
</main>
