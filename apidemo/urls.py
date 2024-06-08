"""
URL configuration for apidemo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from ninja import NinjaAPI

api = NinjaAPI()


@api.get(path="/add",response=int)
async def add(request, a: int, b: int):
    return a + b

import asyncio

import time

@api.get("/say-after-sync")
def say_after(request, delay: int, word: str):
    time.sleep(delay)
    return {"saying": word}

@api.get("/say-after-async")
async def say_after(request, delay: int, word: str):
    await asyncio.sleep(delay)
    return {"saying": word}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
