from django.test import TestCase
from myapp.models import TodoItem


class TodoItemModelTest(TestCase):
    """Test cases for TodoItem model"""
    
    def test_todo_item_creation(self):
        """Test creating a new todo item"""
        todo = TodoItem.objects.create(title="Test todo", completed=False)
        self.assertEqual(todo.title, "Test todo")
        self.assertFalse(todo.completed)
        self.assertIsNotNone(todo.id)
    
    def test_todo_item_default_completed(self):
        """Test that todo items are not completed by default"""
        todo = TodoItem.objects.create(title="Test todo")
        self.assertFalse(todo.completed) 