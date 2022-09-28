from django.urls import path
from file import views
urlpatterns = [

    path('', views.index, name='home'),
    path('login', views.Login, name='login'),
    path('content', views.Download, name='download'),
    path('content/search=<str:search>',views.Search, name='download')

]
