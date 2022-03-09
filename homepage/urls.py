from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home,name='home'),
    path('timeline/', views.timeline, name = 'timeline'),\
    path('news/', views.news, name = 'news'),
    path('<int:pk>/detailed-news/', views.detailed_news, name = 'detailed-news'),
    path('fixtures/<str:fixture_type>/', views.fixtures, name = 'fixtures'),
    path('', include('users.urls')),
    path('',include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
