
<script lang="ts">
    import Card, { Content } from '@smui/card'

    // props
    export let fillForStrip: ReviewStripIf = {
        index: 5.0,
        localHead: "Локация",
        localDescription: "Уточнение локации (если есть)",
        amountDescriptuion: "Кол-во чего-то (отзыв/локация)"
    } 

</script>

<article class="card-container">
    <Card variant="outlined">
        <Content class="strip-layout">
            <p class="review-index">{fillForStrip.index}</p>
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
    .strip-description {
        min-width: 10%;
    }
    .desc-head {
        font-size: large;
        font-weight: bold;
    }

    .review-index {
        text-align: center;
        font-weight: bold;
        /* font-size: 2vw; */
        font-size: 18px;
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
        display: block;
        margin: 10px;
    }
    @media (max-width: 780px) {
        :global(.strip-layout) {
            display: flex;
            justify-content: flex-start;
            align-items: center;
            flex-wrap: wrap;
        }

        .review-count {
            color: gray;
            margin-top: 10px;
        }
    }
</style>
