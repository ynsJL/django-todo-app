from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from myapp.models import TodoItem


class TodosViewTest(TestCase):
    """Test cases for todos view"""
    
    def setUp(self):
        self.client = Client()
        self.todo1 = TodoItem.objects.create(title="Test todo 1", completed=False)
        self.todo2 = TodoItem.objects.create(title="Test todo 2", completed=True)
    
    def test_todos_view_returns_200(self):
        """Test that todos view returns 200 status code"""
        response = self.client.get(reverse('todos'))
        self.assertEqual(response.status_code, 200)
    
    def test_todos_view_uses_correct_template(self):
        """Test that todos view uses the correct template"""
        response = self.client.get(reverse('todos'))
        self.assertTemplateUsed(response, 'todos.html')
    
    def test_todos_view_displays_all_todos(self):
        """Test that todos view displays all todo items"""
        response = self.client.get(reverse('todos'))
        self.assertIn(self.todo1, response.context['todos'])
        self.assertIn(self.todo2, response.context['todos'])
    
    def test_todos_view_post_with_valid_data(self):
        """Test creating a new todo with valid data"""
        response = self.client.post(reverse('todos'), {'task': 'New todo item'})
        self.assertEqual(response.status_code, 200)
        
        # Check if the todo was created
        new_todo = TodoItem.objects.filter(title='New todo item').first()
        self.assertIsNotNone(new_todo)
        self.assertFalse(new_todo.completed)
        
        # Check for success message
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Todo added successfully')
    
    def test_todos_view_post_with_empty_data(self):
        """Test creating a todo with empty data"""
        response = self.client.post(reverse('todos'), {'task': ''})
        self.assertEqual(response.status_code, 200)
        
        # Check for error message
        self.assertIn('error', response.context)
        self.assertEqual(response.context['error'], 'Please input a todo value')
        
        # Check that no new todo was created
        todo_count = TodoItem.objects.count()
        self.assertEqual(todo_count, 2)  # Only the two from setUp 