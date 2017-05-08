from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^games/list/$', views.game_list, name='game_list'),
    url(r'games/(?P<pk>\d+)/$', views.game_single, name='game_single'),
    url(r'^games/new/$', views.game_new, name='game_new'),
]
