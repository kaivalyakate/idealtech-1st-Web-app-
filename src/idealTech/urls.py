"""idealTech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from userdata import views as  user_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', user_views.home, name='home'),
    url(r'^ordermaid/$', user_views.user, name='user'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^maidstat/$', user_views.maidstat, name='maidstat'),
    url(r'^yourorders/$', user_views.yourorders, name='yourorders'),
    url(r'^maidlogin/$', user_views.maiddata, name='maiddata'),
    url(r'^maiddata/$', user_views.maid, name='maid'),
    url(r'^review/$', user_views.reviewmaid, name='reviewmaid'),
    url(r'^message/$', user_views.message, name='message'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
