from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('login/',views.login),
    path('addbook/',views.addbook,name='addbook'),
    path('home/',views.home),
    path('update/<int:id>/',views.update),
    path('delete/<int:id>/',views.delete),

    path('register/', views.register),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)