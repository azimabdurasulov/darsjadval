from django.urls import path
from .views import (
    UchinchiListView,
    UchinchiUpdateView,
    UchinchiDeleteView,
    UchinchiCreateView,
)

urlpatterns = [
    path('<int:pk>/edit/', UchinchiUpdateView.as_view(), name='uchinchi_edit'),
    path('<int:pk>/delete/',UchinchiDeleteView.as_view(), name='uchinchi_delete'),
    path('new/', UchinchiCreateView.as_view(), name='uchinchi_new'),
    path('', UchinchiListView.as_view(), name='uchinchi_list'),
]