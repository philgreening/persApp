from django import forms

class PersForm(forms.Form):
    mms_id = forms.CharField()
    issn = forms.CharField()
    library_name = forms.CharField(max_length=50)
    new_library = forms.CharField(max_length=10)
    location_name = forms.CharField(max_length=20)
    new_location = forms.CharField(max_length=20)
    classmark = forms.CharField(max_length=20)
    new_per_number = forms.CharField()
    # title = forms.CharField(max_length=250, null = False, blank=False)
    holdings_and_wants = forms.CharField(max_length=500)
    new_holdings = forms.CharField(max_length=500)
    new_wants_and_notes = forms.CharField(max_length=500)
    labeled_on_shelf = forms.BooleanField()
    amended_on_alma = forms.BooleanField()