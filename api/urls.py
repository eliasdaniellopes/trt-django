
from django.contrib import admin
from django.urls import path, include
from  registros.views import RegistroViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('registros', RegistroViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls'))
]
