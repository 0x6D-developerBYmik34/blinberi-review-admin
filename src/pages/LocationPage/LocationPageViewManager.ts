import { writable, type Writable } from "svelte/store";



interface LocationProps {
    addres: string,
    brand: string 
}

type ListReviewObj = Array<ReviewObj>

export class LocationPageViewManager {
    url = 'http://127.0.0.1:8000/api/reviews_list' 
    url_loc = 'http://127.0.0.1:8000/api/location' 

    location_id: string
    reviewRatingList: Writable<ListReviewObj> 
    qualityIndex: number
    locationProps: Writable<LocationProps>

    constructor(location_id: string) {
        this.location_id = location_id
        this.reviewRatingList = writable([])
        this.qualityIndex = 1
        this.locationProps = writable({
            brand: "Загрузка",
            addres: "",
        })
    }

    async loadData() {
        const resp = await Promise.all([
            fetch(this.url + `?id=${this.location_id}`),
            fetch(this.url_loc + `?id=${this.location_id}`),
        ])
        const [reviews_list, loc_obj] = await Promise.all(resp.map(r => r.json()))
        this.locationProps.set({
            brand: loc_obj.brand.title,
            addres: loc_obj.addres
        })
        this.qualityIndex = loc_obj.rating
        this.reviewRatingList.set(reviews_list)
        return true
    }

    filterRatingListForData() {}
}
