from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from monitoring import views as monitor_views
from allauth import urls as allauth_urls


urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^accounts/', include(allauth_urls)),
                  url(r'^$', monitor_views.monitor, name='monitoring'),
                  url(r'^monitor/api/get_history/', monitor_views.get_chart, name='get_workers_history'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)