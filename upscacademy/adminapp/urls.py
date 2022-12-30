from django.urls import path
from . import views


urlpatterns = [
    path('admin-login/', views.admin_login, name='admin-login'),
    path('admin-dashbord/', views.admin_dashbord, name='admin-dashbord'),
    path('pending-aspirants/', views.pending_aspirants, name='pending-aspirants'),
    path('accept/<int:id>/',views.accept, name="accept"),
    path('reject/<int:id>/', views.reject, name="reject"),
    path('all-aspirants', views.all_aspirants, name='all-aspirants'),
    path('delete-aspirant/<int:id>',views.delete_aspirant, name="delete-aspirant"),
    path('add-study-material/',views.add_study_material, name='add-study-material'),
    path('manage-study-material/', views.manage_study_material, name='manage-study-material'),
    path('edit-material/<int:id>/', views.edit, name='edit-material'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('add-interview-videos/',views.add_interview_videos, name='add-interview-videos'),
    path('manage-interview-videos/',views.manage_interview_videos, name='manage-interview-videos'),
    path('edit-videos/<int:id>/',views.edit_videos, name='edit-videos'),
    path('delete-videos/<int:id>/',views.delete_videos,name='delete-videos'),
    path('add-mock-test/',views.add_mock_test, name='add-mock-test'),
    path('manage-mock-test/',views.manage_mock_test,name='manage-mock-test'),
    path('edit-mock/<int:id>/', views.edit_mock_test, name='edit-mock'),
    path('delete-mock/<int:id>/',views.delete_mock_test, name= 'delete-mock'),
    path('sentiment-analysis/',views.sentiment_analysis,name='sentiment-analysis'),
    path('sentiment-analysis-graph/',views.sentiment_analysis_graph,name='sentiment-analysis-graph'),
    path('search/',views.searchBar, name='search'),
    path('Material_search/',views.material_details, name='material'),
    path('video_search/', views.videos_details, name='video'),
    path('mock-details/', views.mock_details, name='mock'),
    path('log-out/', views.admin_logout,name='log-out'),
]