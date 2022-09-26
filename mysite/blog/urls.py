from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='list-post'),
    path('about', views.AboutView.as_view(), name='about'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='detail-post'),
    path('post/new', views.PostCreateView.as_view(), name='new-post'),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name='update-post'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='delete-post'),
    path('drafts', views.DraftListView.as_view(), name='list-draft-post'),
    path('post/<int:pk>/comment', views.add_comment_to_post, name='add-comment-to-post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='approve-comment'),
    path('comment/<int:pk>/delete', views.comment_remove, name='delete-comment'),
    path('post/<int:pk>/publish', views.post_publish, name='publish-post'),
]
