from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

import surgery.urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'tt.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(surgery.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
