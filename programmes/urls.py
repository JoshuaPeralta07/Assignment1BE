from rest_framework.routers import DefaultRouter

from programmes.viewsets import ProgrammeViewSet, LecturerViewSet, StudentViewSet, ParentInfoViewSet, \
    StudentTuitionFeeViewSet, StudentMarkViewSet

router = DefaultRouter()
router.register('programme', ProgrammeViewSet, basename='programme')
router.register('lecturer', LecturerViewSet, basename='lecturer')
router.register('student', StudentViewSet, basename='student')
router.register('parentinfo', ParentInfoViewSet, basename='parentinfo')
router.register('studenttuitionfee', StudentTuitionFeeViewSet, basename='studenttuitionfee')
router.register('studentmark', StudentMarkViewSet, basename='studentmark')

urlpatterns = router.urls