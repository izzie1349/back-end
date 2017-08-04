from django.conf.urls import url
from . import views

# TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    # domain.com/basic_app/relative
    url(r'^relative/$', views.relative, name='relative'),
    # domain.com/basic_app/other
    url(r'^other/$', views.other, name='other'),
]
