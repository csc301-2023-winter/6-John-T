from django import forms
from .models import Benches, Park

# code modified from https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/

class BenchesCreateForm(forms.ModelForm):
    class Meta:
        model = Benches
        fields = ['bench_id','bench_title', 'park_id', 'thumbnail']
    
    thumbnail = forms.ImageField(required=False, widget=forms.FileInput)


class BenchesUpdateForm(forms.ModelForm):
    class Meta:
        model = Benches
        # can only modify the bench title and thumbnail, changing the park
        # wouldnt make too much sense given an admin's jurisdiction
        # the bench id is the id of the bench we are to update
        fields = ['bench_id', 'bench_title', 'thumbnail']
    
    thumbnail = forms.ImageField(required=False, widget=forms.FileInput)


class BenchesDeleteForm(forms.ModelForm):
    class Meta:
        model = Benches
        # only takes in the bench id of the bench to be deleted
        fields = ['bench_id']
    