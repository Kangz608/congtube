from django.contrib import admin
from django.urls import path, include
from django.contrib.flatpages import views
from django.contrib.sitemaps.views import sitemap

from config.views import *
from channels.views import *
from users.views import *

from django.conf import settings
from django.conf.urls.static import static

from .sitemaps import StaticViewSitemap
from channels.sitemaps import ChannelSitemap


# Custom Admin Settings
admin.site.site_header = '콩튜브 관리자'
admin.site.index_title = '콩튜브 관리자'
admin.site.site_title = '콩튜브 관리자'



sitemaps = {
        'static': StaticViewSitemap,
        'channels': ChannelSitemap,
}


urlpatterns = [
    # Admin
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('chosim190823/', admin.site.urls),

    # Users
    path('accounts/', include('allauth.urls')),
    path('profile/', ProfileView.as_view(), name='profile'),

    # Template
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),

    # Channels
    path('channels/', include('channels.urls')),

    # Orders
    path('orders/', include('orders.urls')),

    # Star
    path('star/', include('star.urls')),

    # API
    path('api/', include('api.urls')),

    # Flatpages
    path('policy/service/', views.flatpage, {'url': '/policy/service/'}, name='policy-service'),
    path('policy/privacy/', views.flatpage, {'url': '/policy/privacy/'}, name='policy-privacy'),

    # SEO
    path('robots.txt', include('robots.urls')),
    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap',
    )
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
