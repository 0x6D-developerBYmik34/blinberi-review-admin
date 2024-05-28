interface Location {
    rating: number
    amount_reviews: number
    name: string
    addrs: string
}

interface ReviewObj {
    resorce: string
    rating: number
    review: string
    date: string
}

interface City {
    rating: number
    name: string
    amount_locations: number
}

interface LocationsFilter {
    [key: string]: any
    city: number | undefined
    brand: string | undefined
}

interface AdvancedLocationsFilter extends LocationsFilter {
    id: number | undefined
}
