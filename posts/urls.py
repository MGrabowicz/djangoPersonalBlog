from django.urls import path

from .views import createPostView, detailPostView, postsByTagView, searchPosts, homeView

urlpatterns = [
    path('', homeView, name='home'),
    path('create/', createPostView, name='createPost'),
    path('detail/<int:pk>', detailPostView, name='postDetail'),
    path('byTag/<int:pk>', postsByTagView, name='byTag'),
    path('search/', searchPosts, name='search'),
]