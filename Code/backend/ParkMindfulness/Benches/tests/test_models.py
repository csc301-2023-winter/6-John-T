from django.test import TestCase
from django.urls import reverse, resolve
from Benches.models import Benches, Park


class TestModels(TestCase):
    
    def setUp(self):
        self.bench1 = Benches.objects.create(
            bench_id = 1,
            bench_title = 'test bench',
            park_id = Park.objects.create(
                park_id = 1,
                name = 'test park',
                location = 'test location'
            )
        )
        
    def test_bench_model(self):
        self.assertEquals(self.bench1.bench_id, 1)
        self.assertEquals(self.bench1.bench_title, 'test bench')
        self.assertEquals(self.bench1.park_id.park_id, 1)
        self.assertEquals(self.bench1.park_id.name, 'test park')
        self.assertEquals(self.bench1.park_id.location, 'test location')
        
    def test_park_model(self):
        self.assertEquals(self.bench1.park_id.park_id, 1)
        self.assertEquals(self.bench1.park_id.name, 'test park')
        self.assertEquals(self.bench1.park_id.location, 'test location')
    