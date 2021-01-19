from django.forms import ModelForm
from .models import Todo # Todo 모델과 mapping이 될 것이다

class TodoForm(ModelForm) :
    class Meta: # Meta 클래스 정의
        model = Todo
        fields = { 'id', 'content' } # views.py에서 폼을 핸들링하는 함수 이용 -> templates로부터 전돨되는 값의 name과 Meta.model의 fields 이름 동일 & index.html의 속성 이름도 같아야 함 (name)