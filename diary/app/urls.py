from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, TeacherViewSet, GroupViewSet, StudentViewSet, UserLoginView, LoginAPIView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginAPIView.as_view(), name='login'),
]
