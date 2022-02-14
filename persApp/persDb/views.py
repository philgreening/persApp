from django.shortcuts import render
from django.views.generic import TemplateView, ListView, UpdateView
from django.db.models import Q
from .forms import *

from .models import *

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = PeriodicalsOctavo
    template_name = 'search_results.html'

    fields = [
        'mms_id', 'issn', 'library_name',
         'new_library', 'location_name',
         'new_location', 'classmark', 'new_per_number',
         'title', 'holdings_and_wants', 'new_holdings',
         'new_wants_and_notes', 'labeled_on_shelf', 'amended_on_alma'
    ]

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = PeriodicalsOctavo.objects.filter(
            Q(title__icontains=query) | Q(mms_id__icontains=query) | Q(issn__icontains=query)
        )
        return object_list
    
    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)



class UpdatePerView(UpdateView):
    model = PeriodicalsOctavo
    template_name = 'home.html'

    fields = [
        'mms_id', 'issn', 'library_name',
         'new_library', 'location_name',
         'new_location', 'classmark', 'new_per_number',
         'title', 'holdings_and_wants', 'new_holdings',
         'new_wants_and_notes', 'labeled_on_shelf', 'amended_on_alma'
    ]