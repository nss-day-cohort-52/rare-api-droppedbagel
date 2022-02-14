from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rareapi.views import register_user,  login_user
from rest_framework import routers

from rareapi.views.post import PostView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"posts", PostView, "post")

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
