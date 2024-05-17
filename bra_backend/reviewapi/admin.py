from django.contrib import admin

from .models import *


@admin.action(description="Включить обьеткы в учёт рейтинга")
def active_on_rank_true(modeladmin, request, queryset):
    queryset.update(active_on_rank=True)


@admin.action(description="Исключить обьеткы из учёта в рейтинге")
def active_on_rank_false(modeladmin, request, queryset):
    queryset.update(active_on_rank=False)


# Register your models here.

@admin.register(Brand)
class BrandViewAdmin(admin.ModelAdmin):
    exclude = ["active_on_rank"]
    list_display = ["active_on_rank", "title", "desctiption"]
    list_display_links = ["active_on_rank", "title"]
    actions = [active_on_rank_true, active_on_rank_false]


@admin.register(City)
class CityViewAdmin(admin.ModelAdmin):
    list_display = ["name", "tel_city_code"]


@admin.register(Location)
class LocationViewAdmin(admin.ModelAdmin):
    exclude = ["active_on_rank"]
    list_display = [
        "active_on_rank", 
        "addres", 
        "point",
        "brand_with_active",
        "city",
        ]
    list_display_links = ["active_on_rank", "addres", "point"] 
    actions = [active_on_rank_true, active_on_rank_false]

    @admin.display(description="Бренд")
    def brand_with_active(self, obj):
        mark = "✅" if obj.brand.active_on_rank else "❌"
        return f"{obj.brand.title} ({mark})"


@admin.register(Review)
class ReviewViewAdmin(admin.ModelAdmin):
    list_display = [
        "loc_point", 
        "date", 
        "rating",
        "resorce",
        ]
    list_display_links = ["date"] 

    @admin.display(description="геометка")
    def loc_point(self, obj):
        return obj.location.point


# bbradmin
# admin
