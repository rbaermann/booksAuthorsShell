from django.conf.urls import url
from . import views
                
urlpatterns = [
    url(r'^$', views.index),
    url(r'^addbook$', views.addbook),
    url(r'^(?P<bookID>\d+)/desc$', views.bookDesc),
    url(r'^(?P<bookID>\d+)/addauthor$', views.bookAuthor),
    url(r'^(?P<bookID>\d+)/destroy$', views.destroy),
    url(r'^author$', views.author),
    url(r'^authors/addauthor$', views.addauthor),
    url(r'^author/(?P<authorID>\d+)/desc$', views.authorDesc),
    url(r'^author/(?P<authorID>\d+)/addbook$', views.authorBook),
    url(r'^author/(?P<authorID>\d+)/destroy$', views.destroyAuthor),
]