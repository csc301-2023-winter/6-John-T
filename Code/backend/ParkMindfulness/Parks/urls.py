"""Parks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Parks import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    #################
    # REST API URLS #
    #################

    # admin side urls (all require authentication)
    path("create_admin_park/", views.ParkCreateView_admin.as_view(), name="create-admin-park"),
    path("get_all_admin_parks/", views.ParkGetAllView_admin.as_view(), name="get-all-admin-parks"),
    path("update_admin_park/<int:park_id>/", views.ParkUpdateView_admin.as_view(), name="update-admin-park"),
    path("delete_admin_park/<int:park_id>/", views.ParkDeleteView_admin.as_view(), name="delete-admin-park"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)