from django.contrib import admin
from django.urls import path,include
from django.conf import settings 
from django.conf.urls.static import static


urlpatterns = [
    path('admincofee/', admin.site.urls),
    path('', include('mycofee.urls')),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT ) 
