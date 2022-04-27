from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('dashboard',views.dashboard,name="dashboard"),
    path('write',views.write,name="write"),
    path('getMessagesall',views.getMessagesall,name="getMessagesall"),
    path('readall',views.readall,name="readall"),
    path('getMessagesnew',views.getMessagesnew,name="getMessagesnew"),
    path('readnew',views.readnew,name="readnew"),
    path('sendMessage',views.sendMessage,name="sendMessage"),
    path('cleannew',views.cleannew,name="cleannew"),
]