from django.urls import path
from .views import (
    KechkiListView,
    KechkiUpdateView,
    KechkiDeleteView,
    KechkiCreateView,
)

urlpatterns = [
    path('<int:pk>/edit/', KechkiUpdateView.as_view(), name='kechki_edit'),
    path('<int:pk>/delete/',KechkiDeleteView.as_view(), name='kechki_delete'),
    path('new/', KechkiCreateView.as_view(), name='kechki_new'),
    path('', KechkiListView.as_view(), name='kechki_list'),
]