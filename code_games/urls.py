from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.game_list, name='game_list'),
    url(r'(?P<pk>\d+)/$', views.game_single, name='game_single'),
    url(r'^new/$', views.game_new, name='game_new'),
]
