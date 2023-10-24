from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import *


urlpatterns=[
    path('login/',TokenObtainPairView.as_view(),name='token_obtain'),
    path('refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('creatuser',UserRegistrationAPI.as_view()),
    path('me/',me,name='me'),
    path('friends/request/<int:pk>',sent_friend_request,name='sent_friend_request'),
    path('friends/<int:pk>',friends,name='friends'),
    path('friends/<int:pk>/<str:status>',handle_request,name='handle_request')
]