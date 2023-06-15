from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views

urlpatterns = [
    path('', include('frontend.urls')),
    path('logout/', views.LogoutView.as_view(), name= 'logout'),
    path('login/', views.LoginView.as_view(template_name='frontend/login.html'), name= 'login'),

    # path('userprofile/', include('userprofile.urls')),
    # path('users/', include('personnel.urls')), # for all users incl. customer, teller, manager
    # path('patients/', include('patient.urls')), 
    
    # path('*'), url that does not exist
]
