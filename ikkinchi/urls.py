from django.urls import path
from .views import (
    IkkinchiListView,
    IkkinchiUpdateView,
    IkkinchiDeleteView,
    IkkinchiCreateView,
)

urlpatterns = [
    path('<int:pk>/edit/', IkkinchiUpdateView.as_view(), name='ikkinchi_edit'),
    path('<int:pk>/delete/',IkkinchiDeleteView.as_view(), name='ikkinchi_delete'),
    path('new/', IkkinchiCreateView.as_view(), name='ikkinchi_new'),
    path('', IkkinchiListView.as_view(), name='ikkinchi_list'),
]