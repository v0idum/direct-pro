from django.urls import path

from .views import ExpertCreateView, ExpertDetailView, CategoryDetailView

urlpatterns = [
    path('become/', ExpertCreateView.as_view(), name='expert_create'),
    path('<uuid:pk>/', ExpertDetailView.as_view(), name='expert_detail'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail')
]
