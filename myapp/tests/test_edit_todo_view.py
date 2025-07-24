from django.test import TestCase, Client
from django.urls import reverse
from myapp.models import TodoItem
import json


class EditTodoViewTest(TestCase):
    """Test cases for edit_todo view"""
    
    def setUp(self):
        self.client = Client()
        self.todo = TodoItem.objects.create(title="Original title", completed=False)
    
    def test_edit_todo_view_with_valid_data(self):
        """Test editing a todo with valid data"""
        response = self.client.post(reverse('edit_todo'), {
            'modal-title': 'Updated title',
            'id': self.todo.id
        })
        
        self.assertEqual(response.status_code, 200)
        
        # Parse JSON response
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertEqual(data['message'], 'Updated the task succcessfully')
        
        # Verify todo was updated
        self.todo.refresh_from_db()
        self.assertEqual(self.todo.title, 'Updated title')
    
    def test_edit_todo_view_with_empty_title(self):
        """Test editing a todo with empty title"""
        response = self.client.post(reverse('edit_todo'), {
            'modal-title': '',
            'id': self.todo.id
        })
        
        self.assertEqual(response.status_code, 200)
        
        # Parse JSON response
        data = json.loads(response.content)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 'Please input a task')
        
        # Verify todo was not changed
        self.todo.refresh_from_db()
        self.assertEqual(self.todo.title, 'Original title')
    
    def test_edit_todo_view_with_same_title(self):
        """Test editing a todo with the same title"""
        response = self.client.post(reverse('edit_todo'), {
            'modal-title': 'Original title',
            'id': self.todo.id
        })
        
        self.assertEqual(response.status_code, 200)
        
        # Parse JSON response
        data = json.loads(response.content)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 'Equal')
    
    def test_edit_todo_view_with_invalid_id(self):
        """Test editing a todo with invalid id"""
        response = self.client.post(reverse('edit_todo'), {
            'modal-title': 'Updated title',
            'id': 999
        })
        
        self.assertEqual(response.status_code, 404)
    
    def test_edit_todo_view_get_request(self):
        """Test that GET request returns error"""
        response = self.client.get(reverse('edit_todo'))
        
        self.assertEqual(response.status_code, 200)
        
        # Parse JSON response
        data = json.loads(response.content)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 'Invalid request') 