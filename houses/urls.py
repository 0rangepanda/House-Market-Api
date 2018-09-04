from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from houses import views

app_name="houses"

urlpatterns = [
    url(r'^houses/$', views.HouseList.as_view(), name='house-list'),
    url(r'^houses/(?P<pk>[0-9]+)/$', views.HouseDetail.as_view(), name='house-detail'),
]
