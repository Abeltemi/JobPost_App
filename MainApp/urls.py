from django.urls import path
from MainApp import views
urlpatterns = [
    path('', views.job_post, name='home'),
    path('job/<int:id>/', views.job_detail, name='job_detail')
]
