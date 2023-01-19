from django.urls import path

from funny.views import home
from funny.views import contacts
from funny.apps import FunnyConfig

app_name = FunnyConfig.name

urlpatterns = [
    path('', home),
    path('contacts/', contacts)
]