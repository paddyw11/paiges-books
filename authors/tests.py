from django.test import TestCase
from .models import Author
from .forms import AuthorForm
from django.urls import reverse
from django.contrib.auth.models import User


class AuthorModelTests(TestCase):

    def setUp(self):
        """Create a sample author"""
        self.author = Author.objects.create(
            name="John Doe",
            nationality="British",
            bio="John Doe is a famous British author."
        )

    def test_author_creation(self):
        """Test that an author can be created and retrieved correctly"""
        author = Author.objects.get(name="John Doe")
        self.assertEqual(author.nationality, "British")
        self.assertEqual(str(author), "John Doe")

    def test_unique_author_name(self):
        """Test that the author's name must be unique"""
        with self.assertRaises(Exception):
            Author.objects.create(
                name="John Doe",
                nationality="American",
                bio="Another John Doe."
            )


class AuthorFormTests(TestCase):
    
    def test_valid_form(self):
        """Test that the form is valid with correct data"""
        form_data = {
            'name': 'Jane Smith',
            'nationality': 'American',
            'bio': 'Jane Smith is an American author.'
        }
        form = AuthorForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_invalid_form_missing_fields(self):
        """Test that the form is invalid when required fields are missing"""
        form_data = {
            'name': 'Jane Smith',  
        }
        form = AuthorForm(data=form_data)
        self.assertFalse(form.is_valid())
    
    def test_form_saves_correctly(self):
        """Test that the form saves an author correctly"""
        form_data = {
            'name': 'Alice Walker',
            'nationality': 'American',
            'bio': 'Alice Walker is an American novelist.'
        }
        form = AuthorForm(data=form_data)
        if form.is_valid():
            author = form.save()
            self.assertEqual(author.name, 'Alice Walker')

class AuthorViewTests(TestCase):

    def setUp(self):
        """Set up a sample author and a superuser for testing"""
        self.author = Author.objects.create(
            name="John Keats",
            nationality="English",
            bio="John Keats was a major English Romantic poet."
        )
        self.superuser = User.objects.create_superuser(
            username='admin', password='admin', email='admin@example.com'
        )
    
    def test_authors_view(self):
        """Test the authors list view"""
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Keats")
        self.assertTemplateUsed(response, 'authors/authors.html')
    
    def test_author_bio_view(self):
        """Test the author bio detail view"""
        response = self.client.get(reverse('author_bio', args=[self.author.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Keats")
        self.assertTemplateUsed(response, 'authors/author_bio.html')
    
    def test_add_author_view_superuser(self):
        """Test that a superuser can add an author"""
        self.client.login(username='admin', password='admin')
        response = self.client.post(reverse('add_author'), {
            'name': 'George Orwell',
            'nationality': 'British',
            'bio': 'George Orwell was a British writer.'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after successful addition
        self.assertTrue(Author.objects.filter(name='George Orwell').exists())
    
    def test_add_author_view_no_superuser(self):
        """Test that a non-superuser cannot add an author"""
        response = self.client.get(reverse('add_author'))
        login_url = reverse('account_login')
        self.assertEqual(response.status_code, 302)  # Redirects to login or home
        expected_redirect = f'{login_url}?next={reverse("add_author")}'
        self.assertRedirects(response, expected_redirect)
    
    def test_edit_author_view(self):
        """Test editing an author as a superuser"""
        self.client.login(username='admin', password='admin')
        response = self.client.post(reverse('edit_author', args=[self.author.id]), {
            'name': 'John Keats',
            'nationality': 'English',
            'bio': 'An updated bio for John Keats'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after successful edit
        self.author.refresh_from_db()
        self.assertEqual(self.author.bio, 'An updated bio for John Keats')
    
    def test_delete_author_view(self):
        """Test deleting an author as a superuser"""
        self.client.login(username='admin', password='admin')
        response = self.client.post(reverse('delete_author', args=[self.author.id]))
        self.assertEqual(response.status_code, 302)  # Should redirect after successful deletion
        self.assertFalse(Author.objects.filter(id=self.author.id).exists())