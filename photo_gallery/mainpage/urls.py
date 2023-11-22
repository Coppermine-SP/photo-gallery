from django.urls import path # 이것도 어디 sys에 django.http랑 같이 있겠지...?
from . import views # 같은 디렉토리에 있는 views.py 파일을 불러옴.

urlpatterns = [
	path('', views.index, name='index'), # view.py 안에 내가 만들어둔 index라는 함수를 데려왔네
]