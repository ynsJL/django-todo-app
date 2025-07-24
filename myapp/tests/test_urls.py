from django.test import TestCase
from django.urls import reverse


class URLPatternsTest(TestCase):
    """Test cases for URL patterns"""
    
    def test_home_url_pattern(self):
        """Test home URL pattern"""
        url = reverse('home')
        self.assertEqual(url, '/')
    
    def test_todos_url_pattern(self):
        """Test todos URL pattern"""
        url = reverse('todos')
        self.assertEqual(url, '/todos/')
    
    def test_toggle_todo_url_pattern(self):
        """Test toggle_todo URL pattern"""
        url = reverse('toggle_todo', args=[1])
        self.assertEqual(url, '/toggle_todo/1/')
    
    def test_delete_todo_url_pattern(self):
        """Test delete_todo URL pattern"""
        url = reverse('delete_todo', args=[1])
        self.assertEqual(url, '/delete_todo/1/')
    
    def test_edit_todo_url_pattern(self):
        """Test edit_todo URL pattern"""
        url = reverse('edit_todo')
        self.assertEqual(url, '/edit_todo/') 