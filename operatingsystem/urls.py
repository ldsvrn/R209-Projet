from lib2to3.pygram import pattern_grammar
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_os),
    path('os/add/', views.add_os),
    path('os/save/', views.save_os),
    path('os/list/', views.list_os),
    path('os/details/<int:id>/', views.details),
    path('os/delete/<int:id>/', views.delete_os),
    path('os/edit/<int:id>/', views.edit_os),
    path('os/save_edit/<int:id>/', views.save_edit_os),
    path('os/versions', views.list_os_versions),
    
    # URLS VERSIONS
    path('ver/add/', views.add_ver),
    path('ver/save/', views.save_ver),
    path('ver/list/', views.list_ver),
    path('ver/details/<int:id>/', views.details_ver),
    path('ver/delete/<int:id>/', views.delete_ver),
    path('ver/edit/<int:id>/', views.edit_ver),
    path('ver/save_edit/<int:id>/', views.save_edit_ver)
]