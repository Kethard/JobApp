from django.urls import path
from app import views

urlpatterns = [
    path('',views.job_list,name='jobs_home'),
    path('job/<int:id>',views.job, name='job_detail'),
    path('hello/', views.hello, name = 'hello')
]
