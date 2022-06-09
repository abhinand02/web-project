from django.contrib import admin
from django.urls import path,include
from .views import *
# from django.views.static import serve
# from django.conf.urls import url
# from django.conf import settings

urlpatterns = [
    path('index',index,name='index'),
    # path('login', login,name='login'),
    # path('userhome',userhome, name='userhome'),
    path('optout',optout,name='optout'),


    #
    # url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}),
    # url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]