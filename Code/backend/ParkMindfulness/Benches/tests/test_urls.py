from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Benches.views import BenchCreateView_admin, BenchGetView_admin, \
                            BenchGetView_user, BenchGetAllView_admin, \
                            BenchUpdateView_admin, BenchDeleteView_admin

# Need to updated with the correct urls

# class TestUrls(SimpleTestCase):
    
    # Testing the bench create url
    # def test_create_bench_url(self):
    #     url = reverse("create-admin-bench")
    #     self.assertEquals(resolve(url).func.view_class, BenchCreateView_admin)
    
    # Testing the bench view url
    # def test_view_bench_url(self):
    #     url = reverse("get-admin-benches", args=[1])
    #     self.assertEquals(resolve(url), BenchGetView_admin)
        
    # Testing the bench update url
    # def test_update_bench_url(self):
    #     url = reverse("update-admin-bench", args=[1])
    #     self.assertEquals(resolve(url).func, BenchUpdateView_admin)
        
    # Testing the bench delete url
    # def test_delete_bench_url(self):
    #     url = reverse("delete-admin-bench", args=[1])
    #     self.assertEquals(resolve(url).func, BenchDeleteView_admin)
        
    # Testing the bench get all url
    # def test_get_all_benches_url(self):
    #     url = reverse("get-all-admin-benches", args=[1])
    #     self.assertEquals(resolve(url).func, BenchGetAllView_admin)
        
    # #Testing the bench get user url
    # def test_get_user_bench_url(self):
    #     url = reverse("get-user-benches", args=[1])
    #     self.assertEquals(resolve(url).func, BenchGetView_user)
