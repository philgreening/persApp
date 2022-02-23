from django.urls import path

from .views import *

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('search_retention/', RetentionResultsView.as_view(), name='retention_results'),
    path('', HomePageView.as_view(), name='home'),
    path('updated/<int:id>', update_view, name='update'),
    path('almaupdates/', ToUpdateResultsView.as_view(), name='updates'),
    #path('updated/<int:id>', UpdatedView.as_view(), name='updated'),
    # path('updated/', SearchResultsView.as_view(), name='update_per'),
    # path('updated/<int:pk>/', SearchResultsView.as_view(), name='update_per'),

]