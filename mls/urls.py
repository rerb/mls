from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers

from server import views


router = routers.DefaultRouter()
router.register(r'comments', views.CommentViewSet)
router.register(r'languages', views.LanguageViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'votes', views.VoteViewSet)

urlpatterns = patterns('',
                       url(r'^api/', include(router.urls)),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api-auth/',
                           include('rest_framework.urls',
                                   namespace='rest_framework')))
