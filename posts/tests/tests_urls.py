from django.test import TestCase
from django.urls import reverse, resolve
from posts.views import homeView, postsByTagView, createPostView, detailPostView, searchPosts


class TestUrls(TestCase):

    def test_homeUrlIsResolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, homeView)

    def test_createUrlIsResolved(self):
        url = reverse('createPost')
        self.assertEquals(resolve(url).func, createPostView)

    def test_detailUrlIsResolved(self):
        url = reverse('postDetail', args=[1])
        self.assertEquals(resolve(url).func, detailPostView)

    def test_byTagUrlIsResolved(self):
        url = reverse('byTag', args=[1])
        self.assertEquals(resolve(url).func, postsByTagView)

    def test_searchUrlIsResolved(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func, searchPosts)