from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.urls import re_path
from django.views.static import serve

urlpatterns = [
	#path('/login', TemplateView.as_view(template_name='login.html'), name='home'),
	path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', include('card.urls')),
    path('api/',include('card.api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
