from django.http import HttpRequest
from django.shortcuts import render, HttpResponseRedirect

from Utilities.utilities import get_user_data, enter_user_data_to_db


def index(request: HttpRequest):
    return render(request, "home.html")


def click_tracker(request: HttpRequest) -> HttpResponseRedirect:
    data = get_user_data(request)
    enter_user_data_to_db(data)
    return HttpResponseRedirect("https://www.mcdonalds.com/ua/uk-ua.html")
