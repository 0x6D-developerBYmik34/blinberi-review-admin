<script lang="ts">
    import '../style.css'
    import Card from '@smui/card'
    import { params } from "@roxi/routify";
    import QualityIndexWithLoad from "../../components/QualityIndexWithLoad.svelte";
    import MonthRatingChart from "../../components/MonthRatingChart.svelte";
    import TopFiveBrands from "../../components/TopFiveBrands.svelte";

    const URL_CITY_NAME = 'http://127.0.0.1:8000/api/city_name?tel_city_code='

    const filterProp ={
        city: $params.city,
        brand: undefined
    }

    async function loadCityName(city_code: string) {
        const resp = await fetch(URL_CITY_NAME + city_code)
        return await resp.json()
    }
</script>

<main>
    {#await loadCityName(filterProp.city) }
    <p>Загрузка...</p>
    {:then city_name}
    <h1>{city_name}, рейтинг качества</h1>
    {:catch err} 
    <h1>Ошибка!</h1>
    <p>{err}</p>
    {/await}
    <article class="info-container">
        <div class="qi"><QualityIndexWithLoad filterProp={filterProp} /></div>
        <div class="tf"><TopFiveBrands filterProp={filterProp}/></div>
    </article>
    <div class="mchr">
        <Card variant="outlined" padded>
            <MonthRatingChart filterProp={filterProp}/>
        </Card>
    </div>
</main>
