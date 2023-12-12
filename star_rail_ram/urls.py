"""
URL configuration for star_rail_ram project.

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
from django.urls import path, include
from core.views import index, characters, light_cones, character_detail, light_cone_detail

urlpatterns = [
    path('', include('core.urls')),
    path('characters/', characters, name='characters'),
    path('characters/<int:pk>', character_detail, name='character_detail'),
    path('light_cones/', light_cones, name='light_cones'),
    path('light_cones/<int:pk>', light_cone_detail, name='light_cone_detail'),
    path('admin/', admin.site.urls),
]
