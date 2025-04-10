from django.urls import path
from product.views import ListCreateView, RetrieveUpdateDestroyView


urlpatterns = [
    path('list-create', ListCreateView.as_view()),
    path('retreive-update-delete/<int:pk>', RetrieveUpdateDestroyView.as_view()),
]
