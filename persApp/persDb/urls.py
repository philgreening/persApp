from unicodedata import name
from django.urls import path

from .views import *

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', HomePageView.as_view(), name='home'),
    path('updated/<int:pk>', UpdatePerView.as_view(), name='update_per'),
]