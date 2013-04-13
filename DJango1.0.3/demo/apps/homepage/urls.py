from django.conf.urls.defaults import *

urlpatterns=patterns('',

(r'^$','demo.apps.homepage.views.index'),
)
