from ninja import Query, Router

from .models import City, Location, Review
from decimal import *

from .logic import get_review_list_for_loc_id_by_filter, return_ready_loc_rating_list
from .schemas import (
    CityOut,
    LocationForCityListFilter,
    LocationRatingListFilter, 
    LocationRatingMember,
    ReviewListIn,
    ReviewOut
    )


reviewapi_router = Router()


#@reviewapi_router.get("/quality_index")
#def qi_view(): 
#    # либо топортно, либо кеширование хитрое, либо как то ещё
#    ...
#
#@reviewapi_router.get("/top_five")
#def tf_view(): 
#    # либо кеширование, либо реализовать во фронте
#    ...

@reviewapi_router.get(
    "/citys_rating_list",
    response=list[CityOut]
)
def city_list_view(request, filters: Query[LocationForCityListFilter]):
    citys = City.objects.all()

    citys_out = []
    for city in citys:
        city_rank = 0
        loc_len = 0

        locs = filters.filter(
            Location.objects.filter(city=city)
        )

        for loc in locs:
            loc_rating = 0
            amount = 0

            for r in Review.objects.filter(location=loc):
                loc_rating += r.rating
                amount += 1

            loc_rating /= amount

            city_rank += loc_rating
            loc_len += 1

        if not loc_len:
            continue

        city_rank /= loc_len

        out = CityOut(
            rating=Decimal(city_rank).quantize(
                Decimal('.1'), 
                rounding=ROUND_HALF_DOWN
                ),
            amount_locations=loc_len,
            name=city.name,
        )
        citys_out.append(out)

    return citys_out


@reviewapi_router.get(
    "/reviews_list",
    response=list[ReviewOut]
)
def reviews_list_view(request, filters: Query[ReviewListIn]):
    return get_review_list_for_loc_id_by_filter(filters)


@reviewapi_router.get(
    "/location_rating_list", 
    response=list[LocationRatingMember]
)
def location_rating_list_view(request, filters: Query[LocationRatingListFilter]):
    return return_ready_loc_rating_list(filters)
