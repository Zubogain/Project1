from django.urls import path

from .views import HomePageView, delete, edit

urlpatterns = [
    path('delete/<int:id>', delete, name='delete'),
    path('edit/<int:id>', edit, name='edit'),
    path('', HomePageView, name='home'),
]