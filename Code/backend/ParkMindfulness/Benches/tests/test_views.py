from django.test import TestCase, Client
from django.urls import reverse, resolve
from Benches.views import BenchCreateView_admin, BenchGetView_admin, \
                            BenchGetView_user, BenchGetAllView_admin, \
                            BenchUpdateView_admin, BenchDeleteView_admin
from Benches.models import Benches, Audio
from Parks.models import Park

class TestViews(TestCase):
    
    # Set up a bench and park to test
    def setUp(self):
        self.client = Client()
        self.create_url = reverse('create-admin-bench')
        self.update_url = reverse('update-admin-bench', args=['1'])
        self.bench1 = Benches.objects.create(
            bench_id = 1,
            bench_title = 'test bench',
            park_id = Park.objects.create(
                park_id = 1,
                name = 'test park',
                location = 'test location'
            )
        )
    
    # ADMIN VIEWS SHOULD RETURN 401 UNAUTHORIZED AS CLIENT DOES NOT
    # HAVE PERMISSION TO ACCESS THESE VIEWS
    
    # Test the bench create view
    def test_bench_create_view(self):
        response = self.client.get(self.create_url)
        self.assertEquals(response.status_code, 401)
        
    # Test the bench get all view
    def test_bench_get_all_view(self):
        client = Client()
        url = reverse('get-all-admin-benches', args=['1'])
        response = client.get(url)
        self.assertEquals(response.status_code, 401)
        
    # Test the bench get user view
    def test_bench_get_user_view(self):
        client = Client()
        url = reverse('get-user-benches', args=['1'])
        response = client.get(url)
        self.assertEquals(response.status_code, 200)
    
    # Test the bench update view
    def test_bench_update_view(self):
        response = self.client.get(self.update_url)
        self.assertEquals(response.status_code, 401)
        
    # Test the bench delete view
    def test_bench_delete_view(self):
        client = Client()
        url = reverse('delete-admin-bench', args=['1'])
        response = client.get(url)
        self.assertEquals(response.status_code, 401)
