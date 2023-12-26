from django.urls import path
from to_do_list.views import  (ArticleView, ArticleUpdateView, ArticleDeleteView,
                               ProjectIndexView, ProjectDetailView, ProjectCreateView,
                               ProjectUpdateView, ProjectDeleteView, ArticleCreateView)


urlpatterns = [
    # path('', IndexView.as_view(), name='index'),
    # path('articles/add/', ArticleCreateView.as_view(), name='article_create'),
    path('article/<int:pk>/', ArticleView.as_view(), name='article_view'),
    path('article/<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update_view'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete_view'),

    path('', ProjectIndexView.as_view(), name='project_index'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('project/create/', ProjectCreateView.as_view(), name='project_create'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('project/<int:pk>/create-task/', ArticleCreateView.as_view(), name='task_create'),
]

