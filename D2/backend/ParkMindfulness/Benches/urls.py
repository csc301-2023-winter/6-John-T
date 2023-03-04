"""Benches URL Configuration

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
from Benches import views

urlpatterns = [
    #############
    #  A2 URLS  #
    #############
    
    # path("benches-index-test/", views.index, name="test-index"),
    # path("create_bench/", views.bench_create, name="bench_create"),
    # path("view_benches/", views.bench_view, name="bench_view"),
    # path("update_bench/<int:bench_id>/", views.bench_update, name="bench_update"),
    # path("delete_bench/<int:bench_id>/", views.bench_delete, name="bench_delete"),
    # path("create_bench/", views.BenchCreateView.as_view(), name="create-bench"),
    # path("get_benches/<int:park_id>/", views.BenchGetView.as_view(), name="get-benches"),
    # path("update_bench/<int:bench_id>/", views.BenchUpdateView.as_view(), name="update-bench"),
    # path("delete_bench/<int:bench_id>/", views.BenchDeleteView.as_view(), name="delete-bench"),

    #################
    # REST API URLS #
    #################

    # admin side urls (all require authentication)
    path("get_admin_bench/<int:bench_id>/", views.BenchGetView_admin.as_view(), name="get-admin-benches"),
    path("create_admin_bench/", views.BenchCreateView_admin.as_view(), name="create-admin-bench"),
    path("update_admin_bench/<int:bench_id>/", views.BenchUpdateView_admin.as_view(), name="update-admin-bench"),
    path("delete_admin_bench/<int:bench_id>/", views.BenchDeleteView_admin.as_view(), name="delete-admin-bench"),
    path("get_all_admin_benches/<int:park_id>", views.BenchGetAllView_admin.as_view(), name="get-all-admin-benches"),
    path("get_all_admin_parks/", views.ParkGetAllView_admin.as_view(), name="get-all-admin-parks"),

    # user side urls (no authentication required)
    path("get_user_bench/<int:bench_id>/", views.BenchGetView_user.as_view(), name="get-user-benches"),
]