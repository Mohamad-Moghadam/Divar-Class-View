from django.urls import path
from user.views import ListCreateView, RetrieveUpdateDestroyView


urlpatterns = [
    path('create-list', ListCreateView.as_view()),
    path('retrieve-update-delete/<int:pk>', RetrieveUpdateDestroyView.as_view()),
]
