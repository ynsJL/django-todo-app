from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from myapp.models import TodoItem


class ToggleTodoViewTest(TestCase):
    """Test cases for toggle_todo view"""
    
    def setUp(self):
        self.client = Client()
        self.todo = TodoItem.objects.create(title="Test todo", completed=False)
    
    def test_toggle_todo_view_toggles_completed_status(self):
        """Test that toggle_todo view toggles the completed status"""
        # Initially not completed
        self.assertFalse(self.todo.completed)
        
        # Toggle to completed
        response = self.client.get(reverse('toggle_todo', args=[self.todo.id]))
        self.assertEqual(response.status_code, 302)  # Redirect
        
        # Refresh from database
        self.todo.refresh_from_db()
        self.assertTrue(self.todo.completed)
        
        # Toggle back to not completed
        response = self.client.get(reverse('toggle_todo', args=[self.todo.id]))
        self.assertEqual(response.status_code, 302)  # Redirect
        
        # Refresh from database
        self.todo.refresh_from_db()
        self.assertFalse(self.todo.completed)
    
    def test_toggle_todo_view_redirects_to_todos(self):
        """Test that toggle_todo view redirects to todos page"""
        response = self.client.get(reverse('toggle_todo', args=[self.todo.id]))
        self.assertRedirects(response, reverse('todos'))
    
    def test_toggle_todo_view_shows_success_message(self):
        """Test that toggle_todo view shows success message"""
        response = self.client.get(reverse('toggle_todo', args=[self.todo.id]))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Todo updated successfully')
    
    def test_toggle_todo_view_with_invalid_id(self):
        """Test that toggle_todo view handles invalid todo id"""
        response = self.client.get(reverse('toggle_todo', args=[999]))
        self.assertEqual(response.status_code, 404) 