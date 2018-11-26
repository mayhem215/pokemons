from django.conf.urls import url
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
                  url(r'^$', views.post_list, name='list'),
                  url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
                  url(r'^post/new/$', views.post_new, name='post_new'),
                  url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
                  url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
                  path('accounts/', include('django.contrib.auth.urls')),
                  url(r'^register/$', views.register, name='register'),
                  url(r'^loggedout/$', views.logout, name='out'),
                  url(r'^delete/$', views.delete, name='delete'),



              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT, )
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)