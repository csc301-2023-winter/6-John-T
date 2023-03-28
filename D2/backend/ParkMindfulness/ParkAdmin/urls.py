from django.urls import path
from ParkAdmin import views

urlpatterns = [

    #################
    # REST API URLS #
    #################

    path("create_new_admin/", views.NewUserCreateView.as_view(), name="create_new_admin"),
    # path("login_admin/", views.AdminLoginView.as_view(), name="login_admin"),
    # path("logout_admin/", views.AdminLogoutView.as_view(), name="logout_admin"),
    path("update_admin_info/", views.UpdateAdminInfoView.as_view(), name="finish_admin_setup"),
    path("get_admin_info/", views.GetAdminInfoView.as_view(), name="get_admin_info"),
    path("delete_admin/", views.DeleteAdminView.as_view(), name="delete_admin"),
]