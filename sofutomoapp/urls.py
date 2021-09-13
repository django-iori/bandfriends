from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', indexview, name='index'),
    path('signup', signupview, name='signup'),
    path('register/', registerview, name='register'),
    path('login/', loginview, name='login'),
    path('detail/<int:pk>/', detailview, name='detail'),
    path('mypage/', mypageview, name='mypage'),
    path('evaluation/<int:pk>', evaluationview, name='evaluation'),
    path('check/', checkview, name='check'),
    path('host/', hostview, name='host'),
    path('image/', imageview, name='image'),
    path('match/<int:pk>', matchview, name='match'),
    path('chat/<str:room_name>/', chatview, name='chat')
]