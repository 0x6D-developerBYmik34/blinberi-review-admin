<!-- smart component -->

<!-- ротинг для какой то тестовой странички настроить -->
<!-- и дооформить этот компонент -->
<!-- enum в ts, буду задавать в,страице и пробрасывать через пропал компонентам -->

<script lang="ts">
    import ReviewStrip from './ReviewStrip.svelte';
    import Select, { Option } from '@smui/select';

    // props

    // consts
    const testData = [
        {
            index: 5.0,
            localHead: "Фигушки",
            localDescription: "Уточнение локации (если есть)",
            amountDescriptuion: "Кол-во чего-то (отзыв/локация)"
        },
        {
            index: 4.8,
            localHead: "Локация",
            localDescription: "Уточнение локации (если есть)",
            amountDescriptuion: "Кол-во чего-то (отзыв/локация)"
        },
        {
            index: 5.0,
            localHead: "Локация",
            localDescription: "Уточнение локации (если есть)",
            amountDescriptuion: "Кол-во чего-то (отзыв/локация)"
        },
        {
            index: 5.0,
            localHead: "Локация",
            localDescription: "Уточнение локации (если есть)",
            amountDescriptuion: "Кол-во чего-то (отзыв/локация)"
        },
        {
            index: 4.6,
            localHead: "Локация",
            localDescription: "Уточнение локации (если есть)",
            amountDescriptuion: "Кол-во чего-то (отзыв/локация)"
        },
        {
            index: 5.0,
            localHead: "Локация",
            localDescription: "Уточнение локации (если есть)",
            amountDescriptuion: "Кол-во чего-то (отзыв/локация)"
        },
    ]

    const dataOprions = [
        'Февраль 2024',
        'Март 2024',
        'Апрель 2024',
    ]

    let value = dataOprions[dataOprions.length - 1] 
</script>

<article>
    <div class="review-list-head">
        <h3>Рейтинг Локаций</h3>
        <Select variant="outlined" bind:value label="Дата">
          {#each dataOprions as opt}
            <Option value={opt}>{opt}</Option>
          {/each}
        </Select>
    </div>
    <div class="review-list-cont">
        {#each testData as obj }
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
