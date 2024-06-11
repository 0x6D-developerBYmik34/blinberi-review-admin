from typing import Optional
from datetime import date
from django.db.models import Q
from ninja import FilterSchema 
from pydantic import PositiveInt, PastDate


class BrandFilterMixin:
    '''
    Миксин для фильтрации неактивных для рейтинга брендов
    '''
    def filter_brand(self, value: str) -> Q:
        '''фильтрация Brand.active_on_rank'''
        return Q(
            brand=value, 
            brand__active_on_rank=True,
        )


def location_noactive_sifter(
    cls: type[FilterSchema]
    ) -> type[FilterSchema]:
    '''
    Декоратор класса для фильтрации неактивных
    в рейтинге локаций и брендов
    '''
    func = cls.get_filter_expression
    def get_filter_expression(self: FilterSchema) -> Q:
        q = func(self)
        q &= Q(active_on_rank=True)
        q &= Q(brand__active_on_rank=True)
        return q
            
    cls.get_filter_expression = get_filter_expression
    return cls


@location_noactive_sifter
class BrandFilter(FilterSchema, BrandFilterMixin):
    brand: Optional[str] = None 


@location_noactive_sifter
class CityFilter(FilterSchema):
    city: Optional[int] = None


# @location_noactive_sifter
# class LocationRatingListFilter(FilterSchema, BrandFilterMixin):
#     city : Optional[int] = None
#     brand: Optional[str] = None 
#     # город по строке

 
class DateFilter(FilterSchema):
    '''Фильтрация рейтинга по указанной последней дате'''
    given_date: Optional[PastDate] = None

    def filter_given_date(self, value) -> Q:
        return Q(
            date__lt = value
        )


@location_noactive_sifter
class LocationByOptionalIdFilter(FilterSchema):
    id: Optional[PositiveInt] = None


@location_noactive_sifter
class LocationByIdFilter(FilterSchema):
    id: PositiveInt
