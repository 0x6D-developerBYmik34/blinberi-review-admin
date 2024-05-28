from ninja import ModelSchema, Schema
from decimal import Decimal

from .models import Brand, City, Review, Location


class CityOut(Schema):
    rating: Decimal
    name: str
    amount_locations: int


#class LocationRatingMember(Schema):
#    id: int
#    rating: Decimal
#    amount_reviews: int
#    name: str
#    addrs: str
#    brand: str
class CityScheme(ModelSchema):
    class Meta:
        model = City
        exclude = ['tel_city_code']


class BrandScheme(ModelSchema):
    class Meta:
        model = Brand
        exclude = ['desctiption', 'active_on_rank']


class LocationOut(ModelSchema):
    rating: Decimal
    amount_reviews: int
    brand: BrandScheme
    city: CityScheme
    class Meta:
        model = Location
        exclude = ['active_on_rank', 'title', 'brand', 'city']
    

class ReviewOut(ModelSchema):
    class Meta:
        model = Review
        exclude = ['id', 'location']


class BrandWithRankOut(Schema):
    title: str
    rating: Decimal
