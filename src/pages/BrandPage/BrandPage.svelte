<script lang="ts">
    import '../style.css'
    import { params } from "@roxi/routify";
    import MonthRatingChart from "../../components/MonthRatingChart.svelte";
    import QualityIndexWithLoad from "../../components/QualityIndexWithLoad.svelte";
    import RatingListWithFilter from "../../components/RatingListWithFilter.svelte";
    import TopFiveLocations from "../../components/TopFiveLocations.svelte";
    import { BrandPageViewManager } from "./BrandPageViewManager";
    import Card from '@smui/card'

    const viewmanager = new BrandPageViewManager(
        $params['brand']
    )
    const filterProp = {
        brand: $params['brand'],
        city: undefined
    }

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

    let cityRatingStrips: ReviewStripIf[] = []
    viewmanager.cityRatingList.subscribe(
        arr => {
            cityRatingStrips = arr.map(
                obj => ({
                    index: obj.rating,
                    localHead: obj.name,
                    localDescription: "",
                    amountDescriptuion: obj.amount_locations + ' Локаций'
                })
            )
        }
    )

</script>

<main> 
    {#await viewmanager.loadData()}
    <h1>Загрузка...</h1>
    {:then res_ok} 
    <h1>{viewmanager.brand}, рейтинг качества</h1>
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
    <RatingListWithFilter objList={cityRatingStrips} onChangeFilterValue={()=>{}}>
        Рейтинг
    </RatingListWithFilter> 
    {:catch error}
    <h1>Ошибка!</h1>
    <p>{error}</p>
    {/await}  
</main>
