<script lang="ts">
    import TopFive from "./TopFive.svelte";
    import { onMount } from 'svelte'

    const TOP_BRAND_URL = 'http://127.0.0.1:8000/api/top_brands'
    
    export let filterProp: LocationsFilter
    
    let topList = ['Загрузка...']

    onMount(() => {
        let param = '?' + Object
                .entries(filterProp)
                .filter(tup => !!tup[1])
                .map(tup => tup.join('='))
                .join('&')

        fetch(TOP_BRAND_URL + param)
            .then(resp => resp.json())
            .then(brandArr => (
                topList = brandArr.map(
                    obj => obj.title + ' - ' + obj.rating
                )
            ))
            .catch(alert)
    })
</script>

<TopFive topList={topList}>брендов</TopFive>
