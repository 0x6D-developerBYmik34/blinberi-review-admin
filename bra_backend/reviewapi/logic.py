from decimal import *

from django.db.models import Q
from .models import Location, Review
from .schemas import (
    LocationRatingListFilter, 
    LocationRatingMember,
    ReviewListIn,
    ReviewOut
    )


def return_ready_loc_rating_list(
    filters: LocationRatingListFilter
    ) -> list[LocationRatingMember]:
    out_list = []
    
    locs = Location.objects.all()
    f_locs = filters.filter(locs)

    for loc in f_locs:
        loc_rating = 0
        amount = 0
        for r in Review.objects.filter(location=loc):
            loc_rating += r.rating
            amount += 1
        loc_rating /= amount

        out = LocationRatingMember(
            rating=Decimal(loc_rating).quantize(
                Decimal('.1'), 
                rounding=ROUND_HALF_DOWN
                ),
            amount_reviews=amount,
            name=loc.title,
            addrs=loc.addres,
        )
        out_list.append(out)

    return out_list


def get_review_list_for_loc_id_by_filter(
    filters: ReviewListIn
) -> list[ReviewOut]:
    loc = filters.filter(
        Location.objects.all()
        ).get()
    review_set = Review.objects.filter(location=loc)
    return [ReviewOut.from_orm(rev) for rev in review_set]
