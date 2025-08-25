from .views import *
from django.urls import path




urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logouy'),
    path('signup/', RegisterView.as_view(), name='signup'),

    path('users_strike/', UserProfileViewSet.as_view(), name='user_list'),
    path('category/', CategoryAPIView.as_view(), name='user_list'),

    path('lessons/', LessonAPIView.as_view(), name='lesson_lsit'),
    path('certificate/', CertificateAPIView.as_view(), name='lesson_lsit'),

    path('assignment/', AssignmentAPIView.as_view(), name='exams'),
    path('assignment/<int:pk>/', AssignmentDetailAPIView.as_view(), name='exam-detail'),

    path('exam/', ExamAPIView.as_view(), name='exam'),

    path('courses/', CoursesAPIView.as_view(), name='courses_list'),
    path('courses/<int:pk>', CoursesDetailAPIView.as_view(), name='courses_detail'),

    path('review/', ReviewAPIView.as_view(), name='reviews'),

]