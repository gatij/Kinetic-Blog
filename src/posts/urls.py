from django.urls import path, re_path

from . import views as posts_views

app_name='posts'
urlpatterns = [
    re_path(r'^posts/$', posts_views.PostHome, name='index'),#alternative for url()
    re_path(r'^posts/create/$', posts_views.PostCreate, name='create'),
    path(r'posts/detail/<slug:obj_slug>/', posts_views.PostDetail, name='detail'),
    path(r'posts/update/<slug:obj_slug>/', posts_views.PostUpdate, name='update'),
    path(r'posts/delete/<slug:obj_slug>/', posts_views.PostDelete, name='delete'),
    path(r'tags/detail/<slug:tag_slug>/' , posts_views.TagDetail,  name='tag_detail'),
]