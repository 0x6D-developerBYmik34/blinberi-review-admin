import { writable, type Writable } from "svelte/store";


interface BrandCityProps {
    brand: string
    city: string 
}


export class BrandCityPageViewManager {
    url_list = 'http://127.0.0.1:8000/api/location_rating_list' 
    // url_quality = 

    locationRatingList: Writable<Location[]>
    qualityIndex: number
    brandCityProps: Writable<BrandCityProps>
    brand: string
    city_code: string

    constructor(brand: string, city_code: string) {
        this.locationRatingList = writable([])
        this.qualityIndex = 1
        this.brandCityProps = writable({
            brand: brand,
            city: `"(${city_code}), загрузка..."`,
        })
        this.brand = brand
        this.city_code = city_code
    }

    async loadData() {
        const get_params = `?city=${this.city_code}&brand=${this.brand}`
        const resp = await Promise.all([
            fetch(this.url_list + get_params),
        ])
        const [location_list, ] = await Promise.all(
            resp.map(r => r.json())
        )

        this.brandCityProps.update(prop => {
            prop.city = location_list[0].city.name
            return prop
        })

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
        
        return true
    }

    filterRatingListForData() {}
}
