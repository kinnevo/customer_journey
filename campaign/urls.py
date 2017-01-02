__author__ = 'jorgezavala'

from django.conf.urls import url

from campaign import views

urlpatterns = [
    url(r'^campaign', views.campaign, name='campaign'),
    url(r'^start', views.start, name='start'),

    url(r'^create$', views.create, name='create'),
    url(r'^prepare', views.prepare, name='prepare'),
    url(r'^followup', views.followup, name='followup'),
    url(r'^evaluate', views.evaluate, name='evaluate'),
    url(r'^report', views.report, name='report'),

    url(r'^create_newsletter$', views.create_newsletter, name='create_newsletter'),

]
