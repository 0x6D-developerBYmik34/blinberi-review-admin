<script lang="ts">
    import Chart from 'chart.js/auto'
    import { Line } from 'svelte-chartjs'
    import { loadData } from './ChartManager';

    export let filterProp: LocationsFilter
</script>

{#await loadData(filterProp)}
<p>Загрузка...</p> 
{:then data} 
<Line class="chart" {data} options={{ responsive: true }}/>
{:catch err}
<p>err</p>
{/await}

<style>
    :global(.chart) {
        /* padding: 10px; */
        /* width: 1000px; */
        /* height: 500px; */
        /* height: 100%; */
        /* width: 100%; */
    }
</style>
