from django.conf.urls import patterns
from django.contrib.flatpages import views
from django.conf.urls import url


urlpatterns = patterns('website.views',
    url(r'^$', 'home', name="home"),
    url(r'^add-article', 'add_article', name="add-article"),
    url(r'^contact_us', 'contact_us', name="contact"),
    url(r'^article/(?P<article_id>[0-9]+)/$', 'show_article', name='show-article'),
)