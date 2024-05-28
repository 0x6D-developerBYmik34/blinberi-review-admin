import { writable, type Writable } from "svelte/store";


export class BrandPageViewManager {
    url_loc_list = 'http://127.0.0.1:8000/api/location_rating_list' 
    url_city_list = 'http://127.0.0.1:8000/api/citys_rating_list' 
    // url_quality = 

    locationRatingList: Writable<Location[]>
    cityRatingList: Writable<City[]>
    qualityIndex: number
    brand: string

    constructor(brand: string) {
        this.locationRatingList = writable([])
        this.cityRatingList = writable([])
        this.qualityIndex = 1
        this.brand = brand
    }

    async loadData() {
        const get_params = `?brand=${this.brand}`
        const resp = await Promise.all([
            fetch(this.url_loc_list + get_params),
            fetch(this.url_city_list + get_params),
        ])
        const [location_list, city_list] = await Promise.all(resp.map(r => r.json()))

        this.locationRatingList.set(
            location_list.map(loc_obj => {
                return {
                    rating: loc_obj.rating,
                    amount_reviews: loc_obj.amount_reviews,
                    name: loc_obj.id,
                    addrs: loc_obj.addres
                }
            })
        )

        this.cityRatingList.set(city_list)
        
        return true
    }

    filterRatingListForData() {}
}
