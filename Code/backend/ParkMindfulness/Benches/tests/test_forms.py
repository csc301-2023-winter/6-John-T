from django import forms
from django.test import TestCase
from Benches.forms import BenchesCreateForm, BenchesUpdateForm, BenchesDeleteForm
from Benches.models import Benches 
from Parks.models import Park


class TestForms(TestCase):
    
    # Set up a park to be used in the bench tests
    def setUp(self):
        self.park = Park.objects.create(
            park_id = 1,
            name = 'test park',
            location = 'test location'
        )
            
    
    # Test the bench create form
    def test_bench_create_form(self):
        form = BenchesCreateForm(data={
            'bench_id': 1,
            'bench_title': 'test bench',
            'park_id': 1,
            'thumbnail': None
        })
        
        self.assertTrue(form.is_valid())
        
        
    # Test the bench update form
    def test_bench_update_form(self):
        
        bench = Benches.objects.create(
            bench_id = 1,
            bench_title = 'test bench',
            park_id = self.park
        )
        
        form = BenchesUpdateForm(data={
            'bench_id': 1,
            'bench_title': 'updated test bench',
            'thumbnail': None
        })
        
        self.assertTrue(form.is_valid())
        self.assertTrue(form.cleaned_data['bench_title'], 'updated test bench')
        self.assertTrue(Benches.objects.get(bench_id=1).bench_title, 'updated test bench')
        
        
    # Test the bench delete form
    def test_bench_delete_form(self):
        
        bench = Benches.objects.create(
            bench_id = 1,
            bench_title = 'test bench',
            park_id = self.park
        )
        
        form = BenchesDeleteForm(data={
            'bench_id': 1,
        })
        
        self.assertTrue(form.is_valid())
        self.assertTrue(Benches.objects.get(bench_id=1).bench_id, 1)
        