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

class PeriodicalsUKRRStatus(models.Model):
    library_code = models.CharField(max_length=10, null=False, blank=False)
    cycle_name = models.CharField(max_length=10, null=False, blank=False)
    cycle_list_name = models.CharField(max_length=10, null=False, blank=False)
    UKRR_id = models.IntegerField(null=False, blank=False)
    issn_no_hyphen = models.CharField(max_length=10, null=True, blank=True)
    issn = models.CharField(max_length=10, null=True, blank=True)
    title = models.CharField(max_length=250, null = False, blank=False)
    offering = models.CharField(max_length=250, null = False, blank=False)
    supplements = models.CharField(max_length=250, null = True, blank=True)
    gaps = models.CharField(max_length=250, null = True, blank=True)
    shelf_space = models.CharField(max_length=10, null = True, blank=True)
    scarcity = models.CharField(max_length=10, null = True, blank=True)
    holding = models.CharField(max_length=10, null = True, blank=True)
    overlap = models.CharField(max_length=10, null = True, blank=True)
    bl_scarcity = models.CharField(max_length=250, null = True, blank=True)
    bl_scarcity_date = models.CharField(max_length=250, null = True, blank=True)
    ml_scarcity = models.CharField(max_length=250, null = True, blank=True)
    ml_scarcity_date = models.CharField(max_length=250, null = True, blank=True)
    bl_response = models.CharField(max_length=250, null = True, blank=True)
    not_requested = models.CharField(max_length=250, null = True, blank=True)
    holdings_requested = models.CharField(max_length=250, null = True, blank=True)
    date_of_request = models.CharField(max_length=250, null = True, blank=True)
    bl_return_ref = models.CharField(max_length=10, null = False, blank=False)
    bl_overlap = models.CharField(max_length=10, null = False, blank=False)
    retention_status = models.CharField(max_length=20, null = False, blank=False)
    transfer_to_bl = models.CharField(max_length=250, null = True, blank=True)
    retain = models.CharField(max_length=250, null = True, blank=True)
    dispose = models.CharField(max_length=250, null = True, blank=True)

    def __str__(self):
        return self.title






















