from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FacultyViewSet, GroupViewSet, StudentViewSet, KafedraViewSet, SubjectViewSet, TeacherViewSet

router = DefaultRouter()
router.register(r'faculties', FacultyViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'students', StudentViewSet)
router.register(r'kafedras', KafedraViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'teachers', TeacherViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
