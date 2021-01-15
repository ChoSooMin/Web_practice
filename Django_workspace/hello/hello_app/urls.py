from django.urls import path

from . import views # views의 메소드를 사용해야 하므로 import한다

urlpatterns = [
    path('', views.index, name='index'), # 아무것도 없이 요청이 오면 views.index에 들어간다
]