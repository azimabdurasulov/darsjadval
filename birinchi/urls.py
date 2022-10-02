from django.urls import path
from .views import (
    BirinchiListView,
    BirinchiUpdateView,
    BirinchiDeleteView,
    BirinchiCreateView,
)

urlpatterns = [
    path('<int:pk>/edit/', BirinchiUpdateView.as_view(), name='birinchi_edit'),
    path('<int:pk>/delete/',BirinchiDeleteView.as_view(), name='birinchi_delete'),
    path('new/', BirinchiCreateView.as_view(), name='birinchi_new'),
    path('', BirinchiListView.as_view(), name='birinchi_list'),
]