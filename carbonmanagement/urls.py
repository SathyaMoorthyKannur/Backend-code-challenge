from django.contrib import admin
from django.urls import path, include
from carbonapi import views
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
router = DefaultRouter()
router.register('User',views.UserModelViewset,basename='User')
router.register('Usage',views.UsageModelViewset,basename='Usage')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view(),name = 'token_obtain_pair'),
    path('refreshtoken/',TokenRefreshView.as_view(),name = 'refresh_token'),
    path('verifytoken/',TokenVerifyView.as_view(),name = 'token_verify'),
    path('docs/',include_docs_urls(title='Carbon management-api')),
    path('schema',get_schema_view(
        title="Carbon management-api",
        description="API for carbonusage",
        version="1.0.0"
    ),name='openapi-schema'),
]