from django.urls import path

from .views import (
    UserView,
    UserLoginView,
    UserRetrieveUpdateDestroyAPIView,
    ListNumberOfUsersView,
)

urlpatterns = [
    path("accounts/", UserView.as_view()),
    path("accounts/<int:pk>/", UserRetrieveUpdateDestroyAPIView.as_view()),
    path("accounts/newest/<int:num>/", ListNumberOfUsersView.as_view()),
    path("login/", UserLoginView.as_view()),
]
