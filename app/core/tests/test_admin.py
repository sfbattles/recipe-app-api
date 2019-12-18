from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    """Setup function get testcase for testing """
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='richard.long@gmail.com',
            password='password123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='sfbattles@gmail.com',
            password='password123',
            name='richard long'
        )

    def test_users_listed(self):
        """Test that user are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)   # run http get on url

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page work"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        # /admin/core/user/1  sample url that will be created
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
