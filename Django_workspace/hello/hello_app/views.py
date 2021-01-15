from django.shortcuts import render
from django.http import HttpResponse

# controller 역할
# ./templates/*.html은 기본으로 생기는 파일이 아니라 추가할 파일이다 (view의 역할)
# urls.py는 request 들어오는 요청을 url별로 view.py의 함수 mapping을 하는 파일 (추가할 파일)
# Create your views here.

def index(request): # index에 요청이 들어오면 해당되는 request 객체를 사용해서 처리할 수 있다
    return HttpResponse("Hello, world. You're at the Hello Django App index.")