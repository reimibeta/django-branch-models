from django.conf.urls import url
from django.urls import path, include
from branch_models import views
from rest_framework import routers

router = routers.DefaultRouter()
""" branch api """
router.register('branch', views.BranchViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
