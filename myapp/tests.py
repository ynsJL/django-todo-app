# Import all test classes from the tests directory
from .tests.test_models import TodoItemModelTest
from .tests.test_home_view import HomeViewTest
from .tests.test_todos_view import TodosViewTest
from .tests.test_toggle_todo_view import ToggleTodoViewTest
from .tests.test_delete_todo_view import DeleteTodoViewTest
from .tests.test_edit_todo_view import EditTodoViewTest
from .tests.test_urls import URLPatternsTest
from .tests.test_integration import IntegrationTest
