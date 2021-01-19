from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Todo
from .forms import TodoForm

# 이 파일은 MVC 패턴의 controller 역할을 한다
# request로부터 parameter가 넘어온다 (값을 받아서 valid Check 등 다양한 일을 할 수 있음)
# business method 호출 또는 구현
# view(template)에서 참조할 데이터 저장
# view(template) 선택(render)

# todo_app/
def index(request) : # index에 아무런 요청이 들어오지 않았을 때
    # 목록을 가져오고, 일정 리스트에 저장
    todos = Todo.objects.all() # Todo의 모든 데이터를 리턴한다
    context = { "todos": todos } # 데이터를 저장해주는 객체
    return render(request, 'todo_app/index.html', context) # application이 있으면 자동으로 templates 폴더를 찾고, 그 밑의 파일들을 찾는다. (url을 이렇게만 적어도 되는 이유) -> TodoList/settings.py에 설정되어 있음

# todo_app/createTodo
def createTodo(request) :
    # todoContent로 들어오는 데이터를 처리해서 DB에 넣어라
    # 아래 두 문장을 TodoForm을 사용해서 코드 라인을 줄일 수 있다
    # todoContent = request.POST['content'] # dictionary 형태로 넘어온다. key: value
    # new_todo = Todo(content= todoContent) # Todo Model 생성
    new_todo = TodoForm(request.POST) # TodoForm 사용
    new_todo.save() # DB 모델의 저장 메소드
    return HttpResponseRedirect(reverse('index')) # 화면 이동할 필요 없이 index이름을 가진 곳으로 리다이렉트하라

# todo_app/todoList
def todoList(request) :
    pass

# todo_app/deleteTodo
def deleteTodo(request) :
    delete_todo_id = request.GET['id']
    todo = Todo.objects.get(id = delete_todo_id) # Todo Model의 id 검색
    todo.delete() # 삭제
    return HttpResponseRedirect(reverse('index'))

