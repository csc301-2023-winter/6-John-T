from django.urls import path
from ParkAdmin import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    #################
    # REST API URLS #
    #################

    path("create_new_admin/", views.NewUserCreateView.as_view(), name="create_new_admin"),
    path("update_admin_info/", views.UpdateAdminInfoView.as_view(), name="finish_admin_setup"),
    path("get_admin_info/", views.GetAdminInfoView.as_view(), name="get_admin_info"),
    path("delete_admin/", views.DeleteAdminView.as_view(), name="delete_admin"),
]