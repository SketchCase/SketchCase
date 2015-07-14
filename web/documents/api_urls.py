from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from documents.views import DocumentViewSet


router = DefaultRouter()
router.register(r'documents', DocumentViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]