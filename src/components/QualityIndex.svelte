
<!-- это карточка, есть огромный индекс, под ним две подписи -->
<!-- заголовочная и звёздочная -->

<!-- Как будет считаться индекс? какой интерфейс? -->

<script lang="ts">
    import Card, { Content } from '@smui/card'

    // props
    export let isOneLocation = false;
    // export const pageType

    // consts
    const defaultIndex = 4.3;

    let index = defaultIndex;
</script>


<article class="card-container">
    <Card>
        <Content>
            <p class="is_index content_child">{index}</p>
            <h2 class="content_child ch">Индекс качества</h2>
            <p class="pometka content_child">
                *Средний рейтинг локаци{isOneLocation ? "и" : "й"} за текущий месяй, 
                составленный на основе данных всех отзывов 
                пользователей
            </p>
        </Content>
    </Card>
</article>


<style>
    .is_index {
        /* font-size: 120px; */
        font-size: 7vw;
        font-weight: bold;
        text-align: center;
    }

    .content_child {
        margin: 0;
    }

    .pometka {
        color: gray;
    }

    .card-container {
        display: inline-flex;
        align-items: center;

        min-height: 200px;
        width: 250px;
        max-width: 100%;

        padding: 20px;
    }

    .ch {
        margin-bottom: 10px;
    }

</style>
