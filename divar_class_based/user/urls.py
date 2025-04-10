from django.urls import path
from user.views import ListCreateView


urlpatterns = [
    path('create', ListCreateView.as_view()),
    path('list', ListCreateView.as_view()),
]
