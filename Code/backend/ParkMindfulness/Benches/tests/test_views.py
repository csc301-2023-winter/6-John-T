from django.test import TestCase, Client
from django.urls import reverse, resolve
from Benches.RESTviews import BenchCreateView, BenchGetView, BenchUpdateView, BenchDeleteView
from Benches.models import Benches, Park

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.create_url = reverse('bench_create')
        self.update_url = reverse('bench_update', args=['1'])
        self.bench1 = Benches.objects.create(
            bench_id = 1,
            bench_title = 'test bench',
            park_id = Park.objects.create(
                park_id = 1,
                name = 'test park',
                location = 'test location'
            )
        )
    
    def test_bench_create_view(self):
        client = Client()
        url = reverse('bench_create')
        response = client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'create.html')
        
    def test_bench_get_view(self):
        client = Client()
        url = reverse('bench_view')
        response = client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'view.html')
        
    def test_bench_update_view(self):
        client = Client()
        url = reverse('bench_update', args=['1'])
        response = client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'update.html')
        
    def test_bench_delete_view(self):
        client = Client()
        url = reverse('bench_delete', args=['1'])
        response = client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete.html')