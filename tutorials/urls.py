from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.tutorial_landing, name='tutorial_landing',),
    url(r'(?P<pk>\d+)/$', views.tutorial_detail, name='tutorial_detail'),
    url(r'new/$', views.tutorial_new, name='tutorial_new'),
    url(r'(?P<pk>\d+)/edit/$', views.tutorial_edit, name='tutorial_edit'),
]
