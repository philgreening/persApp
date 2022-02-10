from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import *

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = PeriodicalsOctavo
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = PeriodicalsOctavo.objects.filter(
            Q(title__icontains=query) | Q(mms_id__icontains=query) | Q(issn__icontains=query)
        )
        return object_list




