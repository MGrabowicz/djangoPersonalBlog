from django.urls import path

from .views import signupView, loginView, editProfileView

urlpatterns = [
    path('signup/', signupView, name='signup'),
    path('login/', loginView, name='login'),
    path('edit_profile/', editProfileView, name='editProfile'),
]