from django.urls import path
from uploadapp import views

urlpatterns=[
    path('uploads/', views.upload_image, name='addimage'),
    path('file/', views.upload_file, name='addfile'),
    path('thank', views.thank_page, name='thank'),
]