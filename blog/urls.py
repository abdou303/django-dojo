# -*- coding: cp1252 -*-
from django.conf.urls import patterns, url
 
urlpatterns = patterns('blog.views',
    url(r'^home/$', 'home'), # Accueil du blog
    url(r'^article/(?P<id_article>\d+)/$', 'view_article'), # Vue d'un article
    url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/$', 'list_articles'), # Vue des articles d'un mois précis
    url(r'^$', 'tpl'),
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', 'addition'),
)
