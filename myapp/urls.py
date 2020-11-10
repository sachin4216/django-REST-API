# Here we need to use a router
from rest_framework import routers
from . import views
from django.urls import path,include

router = routers.DefaultRouter()
router.register('heroes', views.heroViewSet) #this is link /heros/

urlpatterns = [
    path('', include(router.urls))
]
