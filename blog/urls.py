from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = 'blog'

urlpatterns = [
    # path('',views.post_page,name='posts'),
    path('',PostListView.as_view(), name='postHome'),
    path('blogs/<int:pk>/',PostDetailView.as_view(), name='postDetail'),
    path('blogs/new', PostCreateView.as_view(), name='postNew'),
    path('blogs/<int:pk>/update', PostUpdateView.as_view(), name='postUpdate'),
    path('blogs/<int:pk>/delete', PostDeleteView.as_view(), name='postDelete')


]
