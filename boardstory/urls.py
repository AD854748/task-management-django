# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.StoryListCreateAPIView.as_view(), name='story-list-create-api'),
    path('<int:pk>/', views.StoryRetrieveUpdateDestroyAPIView.as_view(), name='story-retrieve-update-destroy-api'),
]
