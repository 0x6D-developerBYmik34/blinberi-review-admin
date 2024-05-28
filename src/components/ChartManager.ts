
const MOUNTH_RATING_URL = 'http://127.0.0.1:8000/api/quality_index_at_given_date'
const MOUNTH_LABLES_LEN = 14

const monthMs =  30 * 24 * 3600 * 1000

const months = Array
    .from(new Array(MOUNTH_LABLES_LEN))
    .map(
        (value, index) => 
            new Date(Date.now() - monthMs * index)
    )

const dataForChart = {
    labels: months.map(
        date => date.toLocaleString('default', { month: 'long' })
    ).reverse(),
    datasets: [
    {
      label: 'График изменения рейтинга по месяцам',
      fill: true,
      lineTension: 0.3,
      backgroundColor: 'rgba(225, 204,230, .3)',
      borderColor: 'rgb(205, 130, 158)',
      borderCapStyle: 'butt',
      borderDash: [],
      borderDashOffset: 0.0,
      borderJoinStyle: 'miter',
      pointBorderColor: 'rgb(205, 130,1 58)',
      pointBackgroundColor: 'rgb(255, 255, 255)',
      pointBorderWidth: 10,
      pointHoverRadius: 5,
      pointHoverBackgroundColor: 'rgb(0, 0, 0)',
      pointHoverBorderColor: 'rgba(220, 220, 220,1)',
      pointHoverBorderWidth: 2,
      pointRadius: 1,
      pointHitRadius: 10,
      data: [10, 20, 28, 48, 40, 19, 86, 27, 90], // load data tut
    },
    ],
}

export const createDataForChart = 
    () => structuredClone(dataForChart)

export async function loadChartData(
    filterProps: LocationsFilter | AdvancedLocationsFilter
    ) 
{
    let param = '?' + Object
                .entries(filterProps)
                .filter(tup => !!tup[1])
                .map(tup => tup.join('='))
                .join('&')

    param.length !== 1 && (param += '&')

    const resp = await Promise
        .all(
            months.map(
                date => fetch(
                    MOUNTH_RATING_URL + param 
                    + 'given_date=' + date.toISOString().slice(0, 10)
                )
            )
        )
    const rating_list = await Promise
        .all(
            resp.map(r => r.json())
        )
    return rating_list.reverse()
}

export async function loadData(filterProps: LocationsFilter) {
    const data = createDataForChart()
    data.datasets[0].data = await loadChartData(filterProps)
    // data.datasets[0].data = months.map(
    //     () => +(10 * Math.random()).toFixed(1)
    // )
    console.log(data.labels)
    console.log(data.datasets[0].data)

    return data
}
