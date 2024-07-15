from rest_framework.routers import DefaultRouter

from programmes.viewsets import ProgrammeViewSet, LecturerViewSet, StudentViewSet, StudentMarkViewSet, StudentAttendanceViewSet

router = DefaultRouter()
router.register('programme', ProgrammeViewSet, basename='programme')
router.register('lecturer', LecturerViewSet, basename='lecturer')
router.register('student', StudentViewSet, basename='student')
router.register('studentattendance', StudentAttendanceViewSet, basename='studentattendance')
router.register('studentmark', StudentMarkViewSet, basename='studentmark')

urlpatterns = router.urls