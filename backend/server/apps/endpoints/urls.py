from django.http import JsonResponse
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

# import views
from apps.endpoints.views import (
    EndpointViewSet, MLAlgorithmViewSet, MLAlgorithmStatusViewSet,
    MLRequestViewSet, ABTestViewSet, PredictView, StopABTestView
)

router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", EndpointViewSet)
router.register(r"mlalgorithms", MLAlgorithmViewSet)
router.register(r"mlalgorithmstatuses", MLAlgorithmStatusViewSet)
router.register(r"mlrequests", MLRequestViewSet)
router.register(r"abtests", ABTestViewSet)

def root_view(request):
    return JsonResponse({
        "message": "Welcome to the ML API",
        "endpoints": {
            "api": "/api/v1/",
            "docs": "Add link to Swagger or Redoc here (optional)"
        }
    })

urlpatterns = [
    path("", root_view),  # this handles http://127.0.0.1:8000/
    path("api/v1/", include(router.urls)),
    path("api/v1/<str:endpoint_name>/predict", PredictView.as_view(), name="predict"),
    path("api/v1/stop_ab_test/<int:ab_test_id>", StopABTestView.as_view(), name="stop_ab"),
   
]
