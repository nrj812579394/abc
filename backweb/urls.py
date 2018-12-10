from django.conf.urls import url

from backweb import views

urlpatterns = [
    # 文章
    # 添加文章内容
    url(r'^add_art/', views.add_art, name='add'),
    # 文章首页
    url(r'^art/', views.art, name='art_list'),
    # 编辑文章
    url(r'^edit_art/(\d+)/', views.edit_art, name='edit_art'),
    # 删除文章
    url(r'^del_art/(\d+)/', views.del_art, name='del_art'),

    # 注册
    url(r'^register/', views.register),
    # 登陆
    url(r'^login/', views.login),
]