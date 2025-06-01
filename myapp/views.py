from django.shortcuts import render, redirect
from .models import TodoItem
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

def todos(request):
    items = TodoItem.objects.all()
    if request.method == 'POST':
        title = request.POST.get('task')
        if not title:
            return render(request, 'todos.html', {
                'todos': items,
                'error': 'Please input a todo value',
                'old_input': title
            })
        
        # Save the item
        TodoItem.objects.create(title=title, completed=False)
        messages.success(request, 'Todo added successfully')
        return render(request, 'todos.html', {'todos': items})

    return render(request, 'todos.html', {'todos': items})

def toggle_todo(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    messages.success(request, 'Todo updated successfully')
    return redirect('todos')

def delete_todo(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    todo.delete()
    messages.error(request, 'Todo deleted successfully')
    return redirect('todos')  