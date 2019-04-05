from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    # url(r'^news/(\d+)',views.news,name ='news'),
    url(r'^$',views.news_today,name='newsToday'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^new/image$', views.new_news, name='new-news'),
    url(r'^Profile/', views.Profile, name='Profile'),
    
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
