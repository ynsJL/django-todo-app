from django.test import TestCase, Client
from django.urls import reverse


class HomeViewTest(TestCase):
    """Test cases for home view"""
    
    def setUp(self):
        self.client = Client()
    
    def test_home_view_returns_200(self):
        """Test that home view returns 200 status code"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_home_view_uses_correct_template(self):
        """Test that home view uses the correct template"""
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html') 