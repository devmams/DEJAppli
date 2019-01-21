from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url('', include('auth.urls')),
        url('calculdej/', include('calculdej.urls')),
]
