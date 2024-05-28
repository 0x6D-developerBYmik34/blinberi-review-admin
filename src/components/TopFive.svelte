<!-- smart component -->

<script lang="ts">
    import Card, { Content } from '@smui/card'

    export let topList: string[]

    // consts
    const defaultTopLoc = [
        "Блинбери, Гагарина 9",
        "Сушивёсла, Бородинская 3",
        "Хижина суслика, Пушкина 9",
        "Блинбери, Площадь Бородина 6",
        "Сушивёсла, Лесогорская 88",
    ]
</script>

<article class="card-container">
    <Card>
        <Content>
            <p class="top_head">Топ 5 <slot/></p>
            <ul class="top_i_container">
                {#each topList as top_text }
                <li class="top_item">{top_text}</li>
                {/each}
            </ul>
        </Content>
    </Card>
</article>

<style>
    .top_head {
        font-weight: bold;
        text-align: center;
        margin: 0;
        padding: 0;
        margin-bottom: 15px;
    }

    .top_item {
        margin: 0;
        padding: 0;
    }

    .top_i_container {
       margin: 0;
       margin-bottom: 8px;
       padding: 0;
       padding-left: 35px;
       padding-right: 10px;
    }

    .card-container {
        display: inline-flex;
        align-items: center;

        /* min-height: 200px; */
        /* width: 250px; */
        /* max-width: 100%; */

        padding: 10px;
    }

</style>
