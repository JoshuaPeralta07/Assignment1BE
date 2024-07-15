from rest_framework.routers import DefaultRouter

from programmes.viewsets import ProgrammeViewSet, LecturerViewSet, StudentViewSet, StudentAttendanceViewSet, \
    StudentMarkViewSet

router = DefaultRouter()
router.register('programme', ProgrammeViewSet, basename='programme')
router.register('lecturer', LecturerViewSet, basename='lecturer')
router.register('student', StudentViewSet, basename='student')
router.register('student_attendance', StudentAttendanceViewSet, basename='student_attendance')
router.register('student_mark', StudentMarkViewSet, basename='student_mark')

urlpatterns = router.urls
