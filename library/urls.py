from django.conf.urls import url
from . import views

app_name = 'library'

urlpatterns = [
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^$', views.index, name='index'),
    url(r'^books/$', views.books, name='books'),
    url(r'^books/(?P<author_id>[0-9]+)$', views.detail, name='detail'),
    url(r'^all_books/$', views.all_books, name='all_books'),
    url(r'^all_books/(?P<book_id>[0-9]+)$', views.kitapdetayi, name='kitapdetayi'),
    url(r'^publishers/$', views.publishers, name='publishers'),
    url(r'^publishers/(?P<publisher_id>[0-9]+)$', views.publishersdetail, name='publishersdetail'),
]