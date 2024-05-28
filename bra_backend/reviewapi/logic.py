from decimal import *
from datetime import date, timedelta
from functools import lru_cache
import operator
from django.db.models import Q
from .models import Brand, Location, Review, City
from .schemas import (
    BrandWithRankOut,
    CityOut,
    LocationOut,
    ReviewOut
    )


@lru_cache(maxsize=200)
def count_rating_and_amount_for_location(
    review_filter_by_loc: Q
    ) -> tuple[Decimal, int]:
    '''review_filter_by_loc = Q(loc=loc)'''
    loc_rating = 0
    amount = 0
    for r in Review.objects.filter(review_filter_by_loc):
        loc_rating += r.rating
        amount += 1
    loc_rating = amount == 0 or (loc_rating / amount)
    loc_rating = Decimal(loc_rating).quantize(
        Decimal('.1'), 
        rounding=ROUND_HALF_DOWN
    )
    return loc_rating, amount


@lru_cache(maxsize=200)
def count_rank_and_amount_for_locations(
    filter_for_locs: Q, 
    filter_for_reviews: Q = Q()
    ) -> tuple[Decimal, int]:
    count = 0
    out_rank = 0
    for loc in Location.objects.filter(filter_for_locs):
        loc_rating, _ = count_rating_and_amount_for_location(
            Q(location=loc) & filter_for_reviews
        )
        out_rank += loc_rating
        count += 1
    out_rank = count == 0 or (out_rank / count)
    return Decimal(out_rank).quantize(
        Decimal('.1'), 
        rounding=ROUND_HALF_DOWN
    ), count


def get_last_mounth_rank_for_locations(filter_for_locs: Q) -> Decimal:
    fltr = Q(
        date__range = (
            date.today() - timedelta(days=30),
            date.today(),
        )
    )
    return count_rank_and_amount_for_locations(
        filter_for_locs, fltr
    )[0]


def get_rank_for_given_month_for_locations(
    loc_filter: Q,
    datelt: date
    ) -> Decimal:
    fltr = Q(
        date__lt = datelt
    )
    return count_rank_and_amount_for_locations(
        loc_filter, fltr
    )[0]


@lru_cache(maxsize=50)
def get_ready_location_rating_list(
    locations_filter: Q
    ) -> list[LocationOut]:
    out_list = []

    f_locs = Location.objects.filter(locations_filter)

    for loc in f_locs:
        loc_rating, amount = count_rating_and_amount_for_location(
            Q(location=loc)
        )
        out = LocationOut(
            id=loc.id,
            brand=loc.brand,
            city=loc.city,
            rating=Decimal(loc_rating).quantize(
                Decimal('.1'), 
                rounding=ROUND_HALF_DOWN
                ),
            amount_reviews=amount,
            addres=loc.addres,
            point=loc.point,
        )
        out_list.append(out)

    return out_list


def get_top_locations_by_rating(
    locations_filter: Q, 
    top_len: int = 5
    ) -> list[LocationOut]:
    loc_list = get_ready_location_rating_list(
        locations_filter
    )
    return sorted(
        loc_list, 
        key=operator.attrgetter('rating'),
        reverse=True,
    )[:top_len]


def get_city_with_rank_list(filter_for_location: Q) -> list[CityOut]:
    citys = City.objects.all()

    citys_out = []
    for city in citys:
        city_rank, loc_len = count_rank_and_amount_for_locations(
            Q(city=city) & filter_for_location
        )

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


def get_review_list_for_location(
    locations_filter: Q     # its id
) -> list[ReviewOut]:
    loc = Location.objects.filter(locations_filter).get()
    review_set = Review.objects.filter(location=loc)
    return [ReviewOut.from_orm(rev) for rev in review_set]


def get_top_brands_by_rank(
    locations_filter: Q, 
    top_len: int = 5
    ) -> list[BrandWithRankOut]:
    brands = Brand.objects.filter(active_on_rank=True)
    top_list = [
        BrandWithRankOut(
            title=brand.title,
            rating=count_rank_and_amount_for_locations(
                locations_filter & Q(brand=brand)
            )[0]
        ) for brand in brands
    ]
    return sorted(
        top_list, 
        key=operator.attrgetter('rating'),
        reverse=True,
    )[:top_len]
