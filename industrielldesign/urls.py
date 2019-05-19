from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('designsystem.urls')),
    path('', include('home.urls')),
    path('wiki/', include('wiki.urls')),
    path('', include('events.urls')),
    path('', include('projects.urls')),
    path('', include('authentication.urls')),
    path('', include('profilepage.urls')),
    path('', include('courses.urls')),
    path('', include('job.urls')),
    path('', include('books.urls')),
    path('', include('tips.urls'))
]

# handler404 = 'industrielldesign.views.handler404'
# handler500 = 'industrielldesign.views.handler500'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += staticfiles_urlpatterns()
