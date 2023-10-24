from django.urls import path
from .views import *

urlpatterns=[
    path('post_list',PostAPI.as_view()),
    path('post_create',PostAPI.as_view()),
    path('post_on_profile/<int:pk>',PostProfileAPI.as_view()),
    path('search',search,name='search'),
    path('post/like/<int:pk>',like_post,name='like_post'),
    path('post_detail/<int:pk>',post_detail,name='post_detail'),
    path('post/comment/<int:pk>',post_create_comment,name='post_create_comment'),
]