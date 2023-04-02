from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Benches.views import bench_create, bench_view, bench_update, bench_delete


class TestUrls(SimpleTestCase):
    
    def test_create_bench_url(self):
        url = reverse("bench_create")
        self.assertEquals(resolve(url).func, bench_create)
        
    def test_view_bench_url(self):
        url = reverse("bench_view")
        self.assertEquals(resolve(url).func, bench_view)
        
    def test_update_bench_url(self):
        url = reverse("bench_update", args=[1])
        self.assertEquals(resolve(url).func, bench_update)
        
    def test_delete_bench_url(self):
        url = reverse("bench_delete", args=[1])
        self.assertEquals(resolve(url).func, bench_delete)
