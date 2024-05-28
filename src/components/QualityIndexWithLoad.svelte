<script lang='ts'>
    import { onMount } from "svelte";
    import QualityIndex from "./QualityIndex.svelte";

    const qi_url = 'http://127.0.0.1:8000/api/last_quality_index'

    export let filterProp: LocationsFilter

    let qindex = 0

    onMount(() => {
        let param = '?' + Object
                .entries(filterProp)
                .filter(tup => !!tup[1])
                .map(tup => tup.join('='))
                .join('&')
        
        fetch(qi_url + param)
            .then(resp => resp.json())
            .then(index => qindex = index)
            .catch(alert)
    })

</script>

<QualityIndex value={qindex}/>
