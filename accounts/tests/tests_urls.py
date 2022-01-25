from django.test import TestCase
from django.urls import reverse, resolve
from accounts.views import signupView, loginView, editProfileView


class TestUrls(TestCase):

    def test_signUpUrlIsResolved(self):
        url = reverse('signup')
        self.assertEquals(resolve(url).func, signupView)

    def test_loginUrlIsResolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, loginView)

    def test_editProfileUrlIsResolved(self):
        url = reverse('editProfile')
        self.assertEquals(resolve(url).func, editProfileView)