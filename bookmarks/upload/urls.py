from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^imageupload/$', views.uploadation, name='uploadation'),
    url(r'^detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.image_detail, name='detail'),
    url(r'^like/$', views.image_like, name='like'),
]