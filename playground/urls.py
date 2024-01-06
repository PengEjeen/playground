"""
URL configuration for playground project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import *
from scheduleToday.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name="main"),#name요소는 추후 template 연동 시 필요
    path('test/', test, name="test"),
    path('upload/', uploadFile, name="uploadFile"),

    #scheduleToday
    path('scheduleBoard/', scheduleBoard, name="scheduleBoard"),
    path('create_schedule/', create_schedule_view, name='create_schedule'),
    path('delete_Schedule/', delete_Schedule, name='delete_Schedule'),

    #recommend place
    path('recommend_place/', recommend_place, name='recommend_place'),

    #cell page
    path('schedule/<str:schedule_id>/', cell_detail, name='cell_detail'),
    path('schedule/<str:schedule_id>/create_cell/', create_cell, name='create_cell')
]

if settings.DEBUG:
    urlpatterns += static(
            settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)

