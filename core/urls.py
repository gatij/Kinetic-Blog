from django.urls import path, re_path,include
from . import views as core_views
from django.contrib import admin
from django.contrib.auth import views as auth_views
app_name='core'
urlpatterns = [
    re_path(r'^signup/$', core_views.signup, name='signup'),
    re_path(r'^login/$', auth_views.login,{'template_name':'core/login.html'},name='login'),
    re_path(r'^logout/$', auth_views.logout,{'next_page':'posts:index'},name='logout'),
    re_path(r'^update/$', core_views.update_profile,name='update_profile'),
    re_path(r'^profile/$', core_views.myprofile,name='profile'),
    re_path(r'^events/$',core_views.events_detail,name='events_detail'),
    path(r'events/detail/<int:id>/',core_views.detail_of_event,name='detail_of_event'),
    path(r'events/register/<int:id>/',core_views.register_in_event,name='register_in_event'),
    
]