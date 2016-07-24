from django.conf.urls import include, url
from django.contrib import admin
from blog.views import *
import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('blog.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(
            settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
