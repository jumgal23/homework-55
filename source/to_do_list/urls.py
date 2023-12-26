from django.urls import path
from to_do_list.views import  (TaskView, TaskUpdateView, TaskDeleteView,
                               ProjectIndexView, ProjectDetailView, ProjectCreateView,
                               ProjectUpdateView, ProjectDeleteView, TaskCreateView)


urlpatterns = [
    path('', ProjectIndexView.as_view(), name='project_index'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('project/create/', ProjectCreateView.as_view(), name='project_create'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('project/<int:pk>/create-task/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/', TaskView.as_view(), name='task_view'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update_view'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete_view'),
]

