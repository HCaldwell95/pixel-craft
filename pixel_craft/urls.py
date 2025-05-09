from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Include the accounts URLs first
    path('accounts/', include('accounts.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
    path('profile/', views.profile, name='profile'),  # Profile view should come after
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve media files in development (use only in development)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
