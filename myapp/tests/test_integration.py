from django.test import TestCase, Client
from django.urls import reverse
from myapp.models import TodoItem


class IntegrationTest(TestCase):
    """Integration tests for the todo app"""
    
    def setUp(self):
        self.client = Client()
    
    def test_complete_todo_workflow(self):
        """Test the complete workflow: create, toggle, edit, delete"""
        # 1. Create a todo
        response = self.client.post(reverse('todos'), {'task': 'Integration test todo'})
        self.assertEqual(response.status_code, 200)
        
        # Get the created todo
        todo = TodoItem.objects.get(title='Integration test todo')
        self.assertFalse(todo.completed)
        
        # 2. Toggle the todo
        response = self.client.get(reverse('toggle_todo', args=[todo.id]))
        self.assertRedirects(response, reverse('todos'))
        
        todo.refresh_from_db()
        self.assertTrue(todo.completed)
        
        # 3. Edit the todo
        response = self.client.post(reverse('edit_todo'), {
            'modal-title': 'Updated integration test todo',
            'id': todo.id
        })
        self.assertEqual(response.status_code, 200)
        
        todo.refresh_from_db()
        self.assertEqual(todo.title, 'Updated integration test todo')
        
        # 4. Delete the todo
        response = self.client.get(reverse('delete_todo', args=[todo.id]))
        self.assertRedirects(response, reverse('todos'))
        
        # Verify todo was deleted
        self.assertFalse(TodoItem.objects.filter(id=todo.id).exists()) 