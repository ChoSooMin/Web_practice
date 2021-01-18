#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# 0. setting.py, project urls.py 수정 
# 1. todo_with_django repository에 Todo project생성
# 2. Todo project에 my_todo_app application 생성  
# 3. HTML/CSS Javascript 수업에서 작성한 todo  
#    index.html, js/todo.js 파일을 templates로 하는 App작성
# 4. TodoModel : id, content - makemigration, migrate
# 5. views(Controller) 작성(index, createTodo, deleteTodo, clearTodo : todos = Todo.objects.al() todos.delete())
# 6. templates(View) 수정
# 7. application의 urls.py 작성
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Todo.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
