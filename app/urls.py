
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from django.conf.urls import url, include
from app import views
from django.conf.urls import url
from allauth.account.views import confirm_email

urlpatterns = [
    path('upload/', views.upload, name="upload"),
    path('download/', views.download, name="download"),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),
    url(r'^auth/', include('djoser.urls.jwt')),
]
