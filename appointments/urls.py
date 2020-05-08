from django.urls import path
from .views import ListView, DetailView, ServiceListView, ServiceDetailView, CategoryListView, CategoryDetailView, UserDetailView

urlpatterns = [
    path('', ListView.as_view()),
    path('appointments/', ListView.as_view()),
    path('<int:pk>/', DetailView.as_view()),
    path('services/', ServiceListView.as_view()),
    path('services/<int:pk>/', ServiceDetailView.as_view()),
    path('category/', CategoryListView.as_view()),
    path('category/<int:pk>/', CategoryDetailView.as_view()),
    path('user/<int:pk>/', UserDetailView.as_view()),

    # path('user_', display_user_, name='user_')
]
