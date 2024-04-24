
<script lang="ts">
    import Card, { Content } from '@smui/card'

    // props
    export let fillForStrip = {
        index: 5.0,
        localHead: "Локация",
        localDescription: "Уточнение локации (если есть)",
        amountDescriptuion: "Кол-во чего-то (отзыв/локация)"
    } 

    // consts

</script>

<article class="card-container">
    <Card variant="outlined">
        <Content class="strip-layout">
            <p class="review-index">{fillForStrip.index.toFixed(1)}</p>
            <div class="strip-description">
                <p class="desc-head">{fillForStrip.localHead}</p>
                {#if fillForStrip.localDescription }
                <p class="pometka">{fillForStrip.localDescription}</p>
                {/if}
            </div>
            <p class="review-count">{fillForStrip.amountDescriptuion}</p>
        </Content>
    </Card>
</article>

<style>
    .strip-description > * {
        margin: 0;
    }

    .desc-head {
        font-size: large;
        font-weight: bold;
    }

    .review-index {
        text-align: center;
        font-weight: bold;
        font-size: 2vw;
        white-space: nowrap;
    }

    .review-count {
        color:gray;
    }

    .pometka {
        color: gray;
        font-size: 9px;
    }

    :global(.strip-layout) {
        display: flex;
        justify-content: flex-start;
        align-items: center;
    }

    :global(.strip-layout) > * {
        margin: 0;
        padding: 0;
        margin-right: 50px;
    }

    .card-container {
        /* display: inline-flex; */
        /* flex-direction: column; */
        /* align-items: center; */
        display: block;
        margin: 10px;
        /* min-height: 200px; */
        /* width: 250px; */
        /* max-width: 100%; */

        /* padding: 20px; */
    }

</style>
