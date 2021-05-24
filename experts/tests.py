import tempfile

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

from .models import ExpertProfile, Category
from .views import ExpertCreateView


class ExpertTests(TestCase):
    User = get_user_model()

    def setUp(self) -> None:
        self.url = reverse('expert_create')
        self.test_user = self.User.objects.create_user(
            username='testuser',
            email='testuser@email.com',
            password='testpass123'
        )

        self.client.login(email='testuser@email.com', password='testpass123')
        self.response = self.client.get(self.url)
        self.category = Category.objects.create(title='Doctors', slug='doctors')

        self.expert_profile = ExpertProfile.objects.create(
            user=self.test_user,
            first_name='John',
            last_name='Smith',
            category=self.category,
            speciality='Doctor',
            experience_in_years=10,
            about='Very Good Doctor',
            price_per_minute=500000,
            photo=tempfile.NamedTemporaryFile(suffix=".jpg").name
        )

    def test_expert_create_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_expert_create_template(self):
        self.assertTemplateUsed(self.response, 'experts/expert_create.html')

    def test_expert_create_page_contains_correct_html(self):
        self.assertContains(self.response, 'Become an Expert')

    def test_expert_create_url_resolves_expertcreateview(self):
        view = resolve(self.url)
        self.assertEqual(view.func.__name__, ExpertCreateView.as_view().__name__)

    def test_expert_create_form(self):
        self.assertEqual(self.expert_profile.user, self.test_user)
        self.assertEqual(self.expert_profile.first_name, 'John')
        self.assertEqual(self.expert_profile.last_name, 'Smith')
        self.assertEqual(self.expert_profile.category, self.category)
        self.assertEqual(self.expert_profile.speciality, 'Doctor')
        self.assertEqual(self.expert_profile.experience_in_years, 10)
        self.assertEqual(self.expert_profile.about, 'Very Good Doctor')
        self.assertEqual(self.expert_profile.price_per_minute, 500000)

    def test_expert_detail_view(self):
        response = self.client.get(self.expert_profile.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John Smith')
        self.assertContains(response, 'Very Good Doctor')
        self.assertTemplateUsed(response, 'experts/expert_detail.html')
