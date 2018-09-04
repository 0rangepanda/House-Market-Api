from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls

from auth_api import views

# admin and docs
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='Todo API', description='RESTful API for Todo')),
]

# normal apis
urlpatterns += [
    url(r'^$', views.api_root),
    url(r'^api/$', views.api_root),
    url(r'^api/', include('users.urls', namespace='users')),
    url(r'^api/', include('houses.urls', namespace='houses')),
]

# user login api
urlpatterns += [
    url(r'^api/auth/', include('rest_framework.urls')),
]
