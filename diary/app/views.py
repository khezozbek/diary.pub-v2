from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView

from .models import CustomUser, Teacher, Group, Student, ExamResult, Parent
from .serializers import UserSerializer, TeacherSerializer, GroupSerializer, StudentSerializer, \
    ParentSerializer, LoginSerializer
from rest_framework import viewsets
from .models import ExamResult
from .serializers import ExamResultSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token


class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if user:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Missing credentials'}, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(LoginView):
    serializer_class = LoginSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ExamResultViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ExamResult.objects.all()
    serializer_class = ExamResultSerializer

    def create(self, request, *args, **kwargs):
        return Response({"detail": "Method 'POST' not allowed."}, status=405)

    def update(self, request, *args, **kwargs):
        return Response({"detail": "Method 'PUT' not allowed."}, status=405)

    def partial_update(self, request, *args, **kwargs):
        return Response({"detail": "Method 'PATCH' not allowed."}, status=405)

    def destroy(self, request, *args, **kwargs):
        return Response({"detail": "Method 'DELETE' not allowed."}, status=405)


class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
