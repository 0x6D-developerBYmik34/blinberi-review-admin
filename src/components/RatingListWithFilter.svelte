<!-- smart component -->

<script lang="ts">
    import Select, { Option } from '@smui/select';
    import ReviewStrip from './ReviewStrip.svelte';

    // props
    export let objList: ReviewStripIf[]
    export let onChangeFilterValue: () => void

    // consts
    const dataOprions = [
        'Февраль 2024',
        'Март 2024',
        'Апрель 2024',
    ]

    let value = dataOprions[dataOprions.length - 1] 
</script>

<article>
    <div class="review-list-head">
        <h3><slot/></h3>
        <Select on:change={onChangeFilterValue} variant="outlined" bind:value label="Дата">
            {#each dataOprions as opt}
            <Option value={opt}>{opt}</Option>
            {/each}
        </Select>
    </div>
    <div class="review-list-cont">
        {#each objList as obj }
        <ReviewStrip fillForStrip={obj} />
        {/each}
    </div>
</article>

<style>
    .review-list-head {
        display: flex;
        justify-content: flex-start;
        align-items: center;
        margin-bottom: 10px;
    }
    .review-list-head > * {
        margin-left: 30px;
        margin-right: 30px;
    }
    article {
        margin: 10px;
    }
    .review-list-cont {
        display: flex;
        flex-direction: column;
    }
</style>
