from django.conf.urls import url
from smarturls import surl
from . import views

urlpatterns = [
    surl('diary', views.post_list, name='post_list'),
]