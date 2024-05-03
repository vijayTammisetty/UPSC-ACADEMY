from django.urls import path
from . import views

urlpatterns = [
    # path('aspirant_register/', views.aspirant_register, name='register'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('aspirant-register', views.aspirant_register, name='register'),
    path('aspirant-login/', views.aspirant_login, name='login'),
    path('study-material/',views.materials, name='study-material'),
    path('material-details/<int:id>/', views.materials_details_page, name='material-details'),
    path('interview-video/', views.videos, name='interview-video'),
    path('videos-details/<int:id>/', views.videos_details, name='videos-details'),
    path('mock-test', views.mock, name='mock-test'),
    path('mock-details/<int:id>/',views.mock_details, name="mock-details"),
    path('feadback', views.feadback, name='feadback'),
    path('profile', views.profile, name='profile'),
    path('logout/',views.logout, name='logout'),
   

]