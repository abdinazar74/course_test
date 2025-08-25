from .models import *
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import *
from .serializers import *
from rest_framework import viewsets, generics, permissions,status, filters
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django_filters.rest_framework import DjangoFilterBackend
from .permission import CheckRoleReview, CheckRole

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class UserProfileViewSet(generics.ListAPIView):
    serializer_class = UserProfileListSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CoursesAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CoursesListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['level', 'price']
    search_fields = ['course_name']
    ordering_fields = ['price', 'created_at']

class CoursesDetailAPIView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CoursesDetailSerializer

class LessonAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class AssignmentAPIView(generics.ListAPIView):
    queryset = Assingment.objects.all()
    serializer_class = AssignmentListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['level']
    search_fields = ['title']
    ordering_fields = ['type']

class AssignmentDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = Assingment.objects.all()
    serializer_class = AssignmentDetailSerializer

class CertificateAPIView(generics.ListAPIView):
    queryset = Sertificate.objects.all()
    serializer_class = CertificateSerializer

class ExamAPIView(generics.ListAPIView):
    queryset = Sertificate.objects.all()
    serializer_class = CertificateSerializer

class ReviewAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [CheckRoleReview]
