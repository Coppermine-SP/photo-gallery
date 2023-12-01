from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('contributors', views.contributors, name='contributors'),
	path('about', views.about, name='about'),
	path('error', views.error, name='error'),
	path('collections/landscape', views.landscape, name='landscape'),
	path('collections/portrait', views.portrait, name='portrait'),
	path('collections/innovation', views.innovation, name='innovation'),
]