from ninja import Query, Router
from django.db.models import Q
from .models import Location
from decimal import *
from .logic import *
from .schemas import *
from .filter_schemas import *


reviewapi_router = Router()


@reviewapi_router.get(
    "/city_name",
    response=str
)
def get_city_name(request, tel_city_code: int):
    '''tel_city_code - телефонный код города'''
    return City.objects.filter(tel_city_code=tel_city_code).get().name


@reviewapi_router.get(
    "/last_quality_index",
    response=Decimal
)
def last_quality_index_view(
    request, 
    brand_filter: Query[BrandFilter],
    city_filter: Query[CityFilter]
    ): 
    '''
    Посчитает и вернёт средний рейтинг локаций за текущий месяй,
    с фильтрацией по бренду или городу (если указанны).
    Город в формате телефонного кода.
    '''
    return get_last_mounth_rank_for_locations(
        brand_filter.get_filter_expression() 
        & city_filter.get_filter_expression()
    )


@reviewapi_router.get(
    "/quality_index_at_given_date",
    response=Decimal
)
def month_quality_index_view(
    request, 
    date_filter: Query[DateFilter],
    brand_filter: Query[BrandFilter],
    city_filter: Query[CityFilter],
    location_filter: Query[LocationByOptionalIdFilter],
    ): 
    '''
    Посчитает и вернёт средний рейтинг локаций(и) до указанной датe
    с фильтрацией по бренду или городу (если указанны).
    Город в формате телефонного кода.
    '''
    return count_rank_and_amount_for_locations(
        brand_filter.get_filter_expression() 
        & city_filter.get_filter_expression()
        & location_filter.get_filter_expression(),
        date_filter.get_filter_expression()
    )[0]


@reviewapi_router.get(
    "/top_locations",
    response=list[LocationOut]    
)
def top_five_locations_view(
    request,
    brand_filter: Query[BrandFilter],
    city_filter: Query[CityFilter]
    ): 
    '''
    Посчитает и вернёт список топ пяти локаций 
    с фильтрации по бренду или городу (если указанны).
    Город в формате телефонного кода.
    '''
    q = brand_filter.get_filter_expression() & city_filter.get_filter_expression()
    print(q)
    return get_top_locations_by_rating(
        q,
    )


@reviewapi_router.get(
    "/top_brands",
    response=list[BrandWithRankOut]
)
def top_five_brands_view(
    request, 
    city_filter: Query[CityFilter]
    ):
    '''
    Посчитает и вернёт список топ пяти брендов 
    с фильтрацией по городу (если указанн).
    Город в формате телефонного кода.
    '''
    return get_top_brands_by_rank(
        city_filter.get_filter_expression()
    )


@reviewapi_router.get(
    "/citys_rating_list",
    response=list[CityOut]
)
def city_list_view(
    request, 
    brand_filter: Query[BrandFilter],
    ):
    '''
    Вернёт список городов, отсортированных по бренду (если указанн)
    '''
    return get_city_with_rank_list(
        brand_filter.get_filter_expression() 
    )


@reviewapi_router.get(
    "/reviews_list",
    response=list[ReviewOut]
)
def reviews_list_view(
    request, 
    filters: Query[LocationByIdFilter]):
    '''
    Вернёт список отзывов для указанной id локации
    '''
    return get_review_list_for_location(
        filters.get_filter_expression()
    )


@reviewapi_router.get(
    "/location", 
    response=LocationOut
)
def location_view(request, filters: Query[LocationByIdFilter]):
    '''Вернёт ифнормацию о локации по её id'''
    loc = filters.filter(Location.objects.all()).get()
    loc_rating, amount = count_rating_and_amount_for_location(
        Q(location=loc)
    )
    return LocationOut(
        id=loc.id,
        brand=loc.brand,
        city=loc.city,
        rating=loc_rating,
        amount_reviews=amount,
        addres=loc.addres,
        point=loc.point,
    )


@reviewapi_router.get(
    "/location_rating_list", 
    response=list[LocationOut]
)
def location_rating_list_view(
    request, 
    brand_filter: Query[BrandFilter],
    city_filter: Query[CityFilter]
    ):
    '''
    Вернёт список локации с фильтрацией по бренду или городу
    (если указанны). Город в формате телефонного кода.
    '''
    return get_ready_location_rating_list(
        brand_filter.get_filter_expression() 
        & city_filter.get_filter_expression(),
    )
