from django.urls import path
from .views import UserCreateView, CustomLoginView,JobListView, JobCreateView, ApplyForJobView, JobUpdateDeleteView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('jobs/', JobListView.as_view(), name='job-list'),
    path('jobs/create/', JobCreateView.as_view(), name='job-create'),
    path('jobs/<int:pk>/', JobUpdateDeleteView.as_view(), name='job-update-delete'),
    path('jobs/apply/', ApplyForJobView.as_view(), name='job-apply'),
    path('login/', CustomLoginView.as_view(), name='login'),
]
