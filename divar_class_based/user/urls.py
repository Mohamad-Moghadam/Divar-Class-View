from django.urls import path
from user.views import ListCreateView


urlpatterns = [
    path('create-list', ListCreateView.as_view())
]
