from django.urls import path
from product.views import ListCreateView


urlpatterns = [
    path('list-create', ListCreateView.as_view()),
]
