from pyexpat import model
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.db.models import Q
import csv

from .models import *

class HomePageView(TemplateView):
    template_name = 'home.html'

class UpdatedView(DetailView, UpdateView):
    model = PeriodicalsOctavo
    context_object_name = 'per'
    template_name = 'updated.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['per'] = PeriodicalsOctavo.objects.all()
        return context

class SearchResultsView(ListView):
    model = PeriodicalsOctavo
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = PeriodicalsOctavo.objects.filter(
            Q(title__icontains=query) | Q(mms_id__icontains=query) |
            Q(issn__icontains=query) | Q(classmark__icontains=query) |
            Q(new_per_number__icontains=query)
        )
        return object_list

# update view for details
def update_view(request, id):

    obj = get_object_or_404(PeriodicalsOctavo, id = id)

    if request.method == 'POST':
        new_library = request.POST['new_library']
        new_location = request.POST['new_location']
        new_per_number = request.POST['new_per_number']
        new_holdings = request.POST['new_holdings']
        new_wants_and_notes = request.POST['new_wants_and_notes']
        labeled_on_shelf = request.POST['labeled_on_shelf']
        amended_on_alma = request.POST['amended_on_alma']

        obj.new_library = new_library
        obj.new_location = new_location
        obj.new_per_number = new_per_number
        obj.new_holdings = new_holdings
        obj.new_wants_and_notes = new_wants_and_notes
        obj.labeled_on_shelf = labeled_on_shelf
        obj.amended_on_alma = amended_on_alma

        obj.save()

        return render(request,'updated.html',{'per_details': PeriodicalsOctavo.objects.get(id=id)})
    else:
        return render(request,'updated.html',{'per_details': PeriodicalsOctavo.objects.get(id=id)})

class ToUpdateResultsView(ListView):
    model = PeriodicalsOctavo
    template_name = 'alma_updates.html'

    def get_queryset(self):
        # query = self.request.GET.get('q')
        object_list = PeriodicalsOctavo.objects.filter(
            labeled_on_shelf='True',
            amended_on_alma='False'
        )
        return object_list

class RetentionResultsView(ListView):
    model = PeriodicalsUKRRStatus
    template_name = 'retention_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = PeriodicalsUKRRStatus.objects.filter(
            Q(title__icontains=query) | Q(issn__icontains=query)
        )
        return object_list

def export_to_csv(request):
    pers = PeriodicalsOctavo.objects.all()
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="persList_export.csv"'},
    )
    writer = csv.writer(response)
    writer.writerow([
                    'mms_id',
                    'issn',
                    'library_name',
                    'new_library',
                    'location_name',
                    'new_location',
                    'classmark',
                    'new_per_number',
                    'title',
                    'holdings_and_wants',
                    'new_holdings',
                    'new_wants_and_notes',
                    'labeled_on_shelf',
                    'amended_on_alma'
                    ])
    pers_fields = pers.values_list(
                    'mms_id',
                    'issn',
                    'library_name',
                    'new_library',
                    'location_name',
                    'new_location',
                    'classmark',
                    'new_per_number',
                    'title',
                    'holdings_and_wants',
                    'new_holdings',
                    'new_wants_and_notes',
                    'labeled_on_shelf',
                    'amended_on_alma'
                    )
    for pers in pers_fields:
        writer.writerow(pers)

    return response