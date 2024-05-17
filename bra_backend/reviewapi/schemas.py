from typing import Optional
from django.db.models import Q
from ninja import FilterSchema, ModelSchema, Schema
from decimal import Decimal
from pydantic import PositiveInt

from .models import Review


class BrandFilterMixin:
    def filter_brand(self, value: str) -> Q:
        '''фильтрация Brand.active_on_rank'''
        return Q(
            brand=value, 
            brand__active_on_rank=True,
        )


def location_noactive_sifter(cls: type[FilterSchema]):
    func = cls.get_filter_expression
    def get_filter_expression(self: FilterSchema) -> Q:
        q = func(self)
        q &= Q(active_on_rank=True)
        q &= Q(brand__active_on_rank=True)
        return q
            
    cls.get_filter_expression = get_filter_expression
    return cls


@location_noactive_sifter
class LocationForCityListFilter(FilterSchema, BrandFilterMixin):
    brand: Optional[str] = None 


class CityOut(Schema):
    rating: Decimal
    name: str
    amount_locations: int


@location_noactive_sifter
class LocationRatingListFilter(FilterSchema, BrandFilterMixin):
    city : Optional[int] = None
    brand: Optional[str] = None 
    # город по строке


class LocationRatingMember(Schema):
    rating: Decimal
    amount_reviews: int
    name: str
    addrs: str
    

@location_noactive_sifter
class ReviewListIn(FilterSchema):
    id: PositiveInt
    

class ReviewOut(ModelSchema):
    class Meta:
        model = Review
        exclude = ['id', 'location']
