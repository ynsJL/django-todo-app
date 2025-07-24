from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from myapp.models import TodoItem


class DeleteTodoViewTest(TestCase):
    """Test cases for delete_todo view"""
    
    def setUp(self):
        self.client = Client()
        self.todo = TodoItem.objects.create(title="Test todo", completed=False)
    
    def test_delete_todo_view_deletes_todo(self):
        """Test that delete_todo view deletes the todo item"""
        todo_id = self.todo.id
        
        # Verify todo exists
        self.assertTrue(TodoItem.objects.filter(id=todo_id).exists())
        
        # Delete the todo
        response = self.client.get(reverse('delete_todo', args=[todo_id]))
        self.assertEqual(response.status_code, 302)  # Redirect
        
        # Verify todo was deleted
        self.assertFalse(TodoItem.objects.filter(id=todo_id).exists())
    
    def test_delete_todo_view_redirects_to_todos(self):
        """Test that delete_todo view redirects to todos page"""
        response = self.client.get(reverse('delete_todo', args=[self.todo.id]))
        self.assertRedirects(response, reverse('todos'))
    
    def test_delete_todo_view_shows_success_message(self):
        """Test that delete_todo view shows success message"""
        response = self.client.get(reverse('delete_todo', args=[self.todo.id]))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Todo deleted successfully')
    
    def test_delete_todo_view_with_invalid_id(self):
        """Test that delete_todo view handles invalid todo id"""
        response = self.client.get(reverse('delete_todo', args=[999]))
        self.assertEqual(response.status_code, 404) 