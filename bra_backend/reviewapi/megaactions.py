from django.contrib import admin
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.admin.helpers import ACTION_CHECKBOX_NAME
from django import forms
from .models import Review
import datetime


REVIEW_KWARG = {
    "resorce": "тестовые карты",
    "rating": 3,
    "date": datetime.date(
            year=2023,
            month=6,
            day=30,
        ),
    "review": "Нууу такое тип",
}


@admin.action(description="Добавить тестовый отзыв локациям")
def add_simple_review_for_locations(
    modeladmin: admin.ModelAdmin, 
    request, 
    queryset
    ):
    try:
        for loc in queryset:
            r = Review(**REVIEW_KWARG, location=loc)
            print(r, type(r))
            r.save()
        modeladmin.message_user(
            request, 
            "Успешно добавленны два тестовых пользователя",
            messages.SUCCESS,
        )
    except Exception as e:
        modeladmin.message_user(
            request, 
            str(e),
            messages.ERROR,
        )


class ReviewFilterForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    last_date = forms.DateField()
    len_reviews = forms.IntegerField()


@admin.action(description="Добавить детально тестовый отзыв локациям")
def add_detail_review_for_location(
    modeladmin: admin.ModelAdmin, 
    request, 
    queryset
    ):
    print("heeey")
    form = None
    if 'apply' in request.POST:
        form = ReviewFilterForm(request.POST)
        if form.is_valid():
            modeladmin.message_user(
                request, 
                "Успешно добавленны два тестовых пользователя",
                messages.SUCCESS,
            )
            return HttpResponseRedirect(request.get_full_path())
    if not form:
        form = ReviewFilterForm(
            initial={
                '_selected_action': request.POST.getlist(ACTION_CHECKBOX_NAME)
            }
        ) 
    return render(
        request, 
        'load_new_review_detail.html', 
        {'form': form, 'title': 'Изменение категории'}
    )
