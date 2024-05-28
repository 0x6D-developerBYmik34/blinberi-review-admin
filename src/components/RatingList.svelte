<!-- smart component -->

<script lang="ts">
    import ReviewStrip from './ReviewStrip.svelte';
    import { getContext } from 'svelte';

    export let strips: ReviewStripIf[] = []
</script>

<article>
    <h3><slot/></h3>
    <div class="review-list-cont">
        {#each strips as obj }
        <ReviewStrip fillForStrip={obj} />
        {/each}
    </div>
</article>

<style>
    h3 {
        margin-left: 20px;
    }
    .review-list-cont {
        display: flex;
        flex-direction: column;
    }
</style>
