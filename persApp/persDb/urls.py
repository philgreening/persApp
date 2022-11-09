from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import *
from . import views

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('search_retention/', RetentionResultsView.as_view(), name='retention_results'),
    path('', HomePageView.as_view(), name='home'),
    path('updated/<int:id>', login_required(login_url= 'login')(update_view), name='update'),
    path('almaupdates/', ToUpdateResultsView.as_view(), name='updates'),
    path('export_pers_to_csv', views.export_to_csv, name='export_pers_to_csv'),
]