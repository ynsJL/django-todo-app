from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .models import TodoItem

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
    todo = get_object_or_404(TodoItem, id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    messages.success(request, 'Todo updated successfully')
    return redirect('todos')

def delete_todo(request, todo_id):
    todo = get_object_or_404(TodoItem, id=todo_id)
    todo.delete()
    messages.error(request, 'Todo deleted successfully')
    return redirect('todos')

def edit_todo(request):
    if request.method == 'POST':
        title = request.POST.get('modal-title')
        todo_id = request.POST.get('id')

        if not title:
            return JsonResponse({'success': False, 'error': 'Please input a task'})

        todo = get_object_or_404(TodoItem, id=todo_id)

        if todo.title.strip() == title.strip():
            return JsonResponse({'success': False, 'error': 'Equal'})

        todo.title = title
        todo.save()

        return JsonResponse({'success': True, 'message': 'Updated the task succcessfully'})

    return JsonResponse({'success': False, 'error': 'Invalid request'})

def dd(data):
    try:
        dump = json.dumps(data, indent=2, default=str)
    except Exception:
        dump = str(data)
    response = HttpResponse(f"<pre>{dump}</pre>", content_type="text/html")
    # Stop further processing like Laravel dd()
    raise Exception(response)