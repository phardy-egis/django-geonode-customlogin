from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.login_page, name="index"),
    path("appselect", views.app_selection_page, name="appselect"),
]