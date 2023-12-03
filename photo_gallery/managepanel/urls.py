from django.urls import path
from . import views

app_name = "managepanel"
urlpatterns = [
    path('manage', views.manage, name='manage'),
    path('upload', views.upload, name='upload'),
    path('delete', views.delete, name='delete')
]