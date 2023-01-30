from django.urls import path, include
from rest_framework.routers import DefaultRouter

from groups.views.groups import GroupModelViewSet
from groups.views.views import BranchModelViewSet, RoomModelViewSet, CourseModelViewSet, RoleModelViewSet
from users.views import StudentModelViewSet

router = DefaultRouter()
router.register('role', RoleModelViewSet, basename='role')
router.register('course', CourseModelViewSet, basename='course')
router.register('group', GroupModelViewSet, basename='group')
router.register('branch', BranchModelViewSet, basename='branch')
router.register('room', RoomModelViewSet, basename='room')
router.register('student', StudentModelViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
]
