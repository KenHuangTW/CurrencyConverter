from django.urls import path
from .views import CurrencyConverter

urlpatterns = [
    path('currency-converter/', CurrencyConverter.as_view()),
]