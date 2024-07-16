from django.urls import path
from rest_framework.routers import DefaultRouter

from programmes.views import RegisterView
from programmes.viewsets import ProgrammeViewSet, LecturerViewSet, StudentViewSet

router = DefaultRouter()
router.register('programme', ProgrammeViewSet, basename='programme')
router.register('lecturer', LecturerViewSet, basename='lecturer')
router.register('student', StudentViewSet, basename='student')


urlpatterns = router.urls
urlpatterns += [
    path('register/', RegisterView.as_view(), name='register'),
]
