from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('online_shopp.urls')),

    path('auth/', include('dj_rest_auth.urls')),

    path('allauth/', include('allauth.urls')),
    path('accounts/', include('accounts.urls')),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
