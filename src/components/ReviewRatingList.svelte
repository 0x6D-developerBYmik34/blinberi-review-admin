<!-- smart component -->

<script lang="ts">
    import Card, { Content } from '@smui/card'
    import ReviewStrip from './ReviewStrip.svelte';

    // props

    // consts
    const testData = [
        {
            index: 5.0,
            localHead: "2024.02.28",
            localDescription: "Андрей П",
            amountDescriptuion: "Всё отлично"
        },
        {
            index: 5.0,
            localHead: "2024.02.28",
            localDescription: "Андрей П",
            amountDescriptuion: "Всё отлично"
        },
        {
            index: 5.0,
            localHead: "2024.02.28",
            localDescription: "Андрей П",
            amountDescriptuion: "Всё отлично"
        },
        {
            index: 5.0,
            localHead: "2024.02.28",
            localDescription: "Андрей П",
            amountDescriptuion: "Всё отлично"
        },
        {
            index: 5.0,
            localHead: "2024.02.28",
            localDescription: "Андрей П",
            amountDescriptuion: "Всё отлично"
        },
        {
            index: 5.0,
            localHead: "2024.02.28",
            localDescription: "Андрей П",
            amountDescriptuion: "Всё отлично"
        },
        {
            index: 5.0,
            localHead: "2024.02.28",
            localDescription: "Андрей П",
            amountDescriptuion: "Всё отлично"
        },
        {
            index: 5.0,
            localHead: "2024.02.28",
            localDescription: "Андрей П",
            amountDescriptuion: "Всё отлично"
        },
        {
            index: 5.0,
            localHead: "2024.02.28",
            localDescription: "Андрей П",
            amountDescriptuion: "Всё отлично"
        },
        {
            index: 5.0,
            localHead: "2024.02.28",
            localDescription: "Андрей П",
            amountDescriptuion: "Всё отлично"
        },
        {
            index: 5.0,
            localHead: "2024.02.28",
            localDescription: "Андрей П",
            amountDescriptuion: "Всё отлично"
        },
    ]
</script>

<article>
    <h3>Отзывы</h3>
    <div class="review-list-cont">
        {#each testData as obj }
        <ReviewStrip fillForStrip={obj} />
        {/each}
    </div>
</article>

<style>
    .review-list-cont {
        display: flex;
        flex-direction: column;
    }
</style>
