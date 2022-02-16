from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from django.db.models import Q

from .models import *

class HomePageView(TemplateView):
    template_name = 'home.html'

class UpdatedView(TemplateView):
    template_name = 'updated.html'

class SearchResultsView(ListView):
    model = PeriodicalsOctavo
    template_name = 'search_results.html'
   
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = PeriodicalsOctavo.objects.filter(
            Q(title__icontains=query) | Q(mms_id__icontains=query) | Q(issn__icontains=query)
        )
        return object_list
    
    # # update view for details
def update_view(request, id):

    obj = get_object_or_404(PeriodicalsOctavo, id = id)

    if request.method == 'POST':
        new_library = request.POST['new_library']
        new_location = request.POST['new_location']
        new_per_number = request.POST['new_per_number']
        new_holdings = request.POST['new_holdings']
        new_wants_and_notes = request.POST['new_wants_and_notes']
        # labeled_on_shelf = request.POST['labeled_on_shelf']
        # amended_on_alma = request.POST['amended_on_alma']

        obj.new_library = new_library
        obj.new_location = new_location
        obj.new_per_number = new_per_number
        obj.new_holdings = new_holdings
        obj.new_wants_and_notes = new_wants_and_notes
        # obj.labeled_on_shelf = labeled_on_shelf
        # obj.amended_on_alma = amended_on_alma

        obj.save()

        return render(request,'updated.html',{})