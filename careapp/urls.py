
from django.contrib import admin
from django.urls import path
from careapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "index"),
    path('starter/', views.starter, name = "starter"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('appointment/', views.appoint, name="appointment"),
    path('show/', views.show, name="show"),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit)
]
