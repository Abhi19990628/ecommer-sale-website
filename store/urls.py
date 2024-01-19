from django.urls import path
from . import views

urlpatterns = [
	path('index', views.main, name="main"),
	path('mens/', views.mens, name="mens"),
	path('Contact/', views.Contact, name="Contact"),
    path('home/', views.home, name="home"),
]