from django.urls import path
from .views import LoginView, ProfileView, SignupView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view()),
    path('profile/', ProfileView.as_view()),
]