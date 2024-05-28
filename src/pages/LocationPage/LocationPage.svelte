<script lang="ts">
    import '../style.css'
    import { params } from "@roxi/routify";
    import MonthRatingChart from "../../components/MonthRatingChart.svelte";
    import QualityIndex from "../../components/QualityIndex.svelte";
    import RatingList from "../../components/RatingList.svelte";
    import { LocationPageViewManager } from "./LocationPageViewManager";
    import Card from '@smui/card'

    const viewmanager = new LocationPageViewManager($params.loc)
    const filterProp = {
        city: undefined,
        brand: undefined,
        id: $params.loc,
    }

    const locationProps = viewmanager.locationProps 
    $: ({brand, addres} = $locationProps)

    let reviewRatingStrips: ReviewStripIf[] = []
    viewmanager.reviewRatingList.subscribe(
        arr => {
            reviewRatingStrips = arr.map(
                obj => ({
                    index: obj.rating,
                    localHead: obj.date,
                    localDescription: obj.resorce,
                    amountDescriptuion: obj.review
                })
            )
        }
    )

</script>

<main> 
    {#await viewmanager.loadData()}
    <h1>Загрузка...</h1>
    {:then res_ok} 
    <h1>{brand}, {addres}</h1>
    <article class="info-container">
        <div class="qi">
            <QualityIndex value={viewmanager.qualityIndex} isOneLocation={true} />
        </div>
    </article>
    <div class="mchr">
        <Card variant="outlined" padded>
            <MonthRatingChart filterProp={filterProp}/>
        </Card>
    </div>
    <RatingList strips={reviewRatingStrips}>
        Отзывы
    </RatingList>
    {:catch error}
    <h1>Ошибка!</h1>
    <p>{error}</p>
    {/await}  
</main>
