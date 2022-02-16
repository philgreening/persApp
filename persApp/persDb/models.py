from django.db import models
from django.urls import reverse


class PeriodicalsOctavo(models.Model):
    mms_id = models.TextField(null=False, blank=False)
    issn = models.TextField(null=True, blank=True)
    library_name = models.CharField(max_length=50, null=False, blank=False)
    new_library = models.CharField(max_length=10, null=True, blank=True)
    location_name = models.CharField(max_length=20, null=False, blank=False)
    new_location = models.CharField(max_length=20, null=True, blank=True)
    classmark = models.CharField(max_length=20, null=True, blank = True)
    new_per_number = models.CharField(max_length=10, null=True, blank=True)
    title = models.CharField(max_length=250, null = False, blank=False)
    holdings_and_wants = models.CharField(max_length=500, null=False, blank=False)
    new_holdings = models.CharField(max_length=500, null=True, blank=True)
    new_wants_and_notes = models.CharField(max_length=500, null=True, blank=True)
    labeled_on_shelf = models.BooleanField(default=False)
    amended_on_alma = models.BooleanField(default=False)

    def __str__(self):
        return self.mms_id
    
    # def get_absolute_url(self):
    #     return reverse('update_per', kwargs={'pk': self.pk})

