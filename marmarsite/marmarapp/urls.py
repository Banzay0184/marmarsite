from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/<slug:project_slug>', views.PeojectsDetailView.as_view(), name='project_single'),
    path('<slug:slug>/', views.ProjectsListView.as_view(), name='project_list'),
    path('', views.index, name='index'),
]
