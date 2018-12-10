from django.conf.urls import url

from web import views

urlpatterns = [
    url(r'^share/', views.share, name='share'),
    url(r'^my_index/', views.my_index),
]