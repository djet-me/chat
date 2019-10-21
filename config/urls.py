from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic.base import TemplateView

from rest_framework_swagger.views import get_swagger_view

from .api import api_urls


schema_view = get_swagger_view(title='CHAT API')


urlpatterns = [
    path('', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('admin/', admin.site.urls),
    path('chat/', login_required(
            TemplateView.as_view(template_name='index.html'),
            login_url='/'
    )),
] + api_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += [path('api/v1/docs/', schema_view)]
