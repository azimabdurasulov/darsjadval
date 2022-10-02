from django.urls import path
from .views import (
    TurtinchiListView,
    TurtinchiUpdateView,
    TurtinchiDeleteView,
    TurtinchiCreateView,
)

urlpatterns = [
    path('<int:pk>/edit/', TurtinchiUpdateView.as_view(), name='turtinchi_edit'),
    path('<int:pk>/delete/',TurtinchiDeleteView.as_view(), name='turtinchi_delete'),
    path('new/', TurtinchiCreateView.as_view(), name='turtinchi_new'),
    path(' ', TurtinchiListView.as_view(), name='turtinchi_list'),
]