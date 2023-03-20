from django.urls import path
from ParkAdmin import views

urlpatterns = [

    #################
    # REST API URLS #
    #################

    path("create_new_admin/", views.NewUserCreateView.as_view(), name="create_new_admin"),
    path("finish_admin_setup/", views.FinishAdminSetupView.as_view(), name="finish_admin_setup"),
    path("login_admin/", views.AdminLoginView.as_view(), name="login_admin"),
    # path("get_admin_info/<int:admin_id>/", views.GetAdminInfoView.as_view(), name="get_admin_info"),
    # path("update_admin_info/<int:admin_id>/", views.UpdateAdminInfoView.as_view(), name="update_admin_info"),
    # path("delete_admin/<int:admin_id>/", views.DeleteAdminView.as_view(), name="delete_admin"),
]