from django.urls import path

from tracker.views import index, click_tracker

urlpatterns = [
    path("main/", index, name="main"),
    path("ty/", click_tracker, name="ty"),
]


app_name = 'tracker'
