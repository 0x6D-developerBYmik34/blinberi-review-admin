<script lang="ts">
    import TopFive from "./TopFive.svelte";
    import { onMount } from 'svelte'

    const TOP_LOC_URL = 'http://127.0.0.1:8000/api/top_locations'

    export let filterProp: LocationsFilter

    let topList = ['Загрузка...']

    onMount(() => {
        let param = '?' + Object
                .entries(filterProp)
                .filter(tup => !!tup[1])
                .map(tup => tup.join('='))
                .join('&')
        
        fetch(TOP_LOC_URL + param)
            .then(resp => resp.json())
            .then(locArr => (
                topList = locArr.map(
                    obj => obj.addres
                )
            ))
            .catch(alert)
    })
</script>

<TopFive topList={topList}>локаций</TopFive>
