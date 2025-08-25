from .models import *
from rest_framework import serializers
from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                   'role')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class StrikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Strike
        fields = ("date", "is_active")


class UserProfileListSerializer(serializers.ModelSerializer):
    total_strikes = serializers.SerializerMethodField()
    active_days = serializers.SerializerMethodField()
    last_strike = serializers.SerializerMethodField()
    strike_history = StrikeSerializer(source="strikes", many=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'role']
        fields = [
            "id", "username", "last_name",'first_name',
            "total_strikes", "active_days", "last_strike", "strike_history"
        ]

    def get_total_strikes(self, obj):
        return obj.strikes.count()

    def get_active_days(self, obj):
        return obj.strikes.filter(is_active=True).count()

    def get_last_strike(self, obj):
        last = obj.strikes.order_by('-date').first()
        return last.date if last else None



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'content',]

class CoursesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'description','course_name', 'price', 'created_by',]

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class CoursesDetailSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(read_only=True, many=True)
    reviews = ReviewSerializer(read_only=True, many=True)
    created_by = UserProfileSerializer()
    created_at = serializers.DateTimeField(format('%d-%m-%y %H:%M'))
    # category = CategorySerializer()
    category = serializers.SlugRelatedField(many=True,read_only=True, slug_field='category_name')
    class Meta:
        model = Course
        fields = ['id','course_name', 'price', 'created_by',
                  'description','created_at', 'level', 'category', 'lessons', 'reviews']


class AssignmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assingment
        fields = ['id', 'title']


class AssignmentDetailSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer()
    class Meta:
        model = Assingment
        fields = [ 'title', 'description', 'level','due_date', 'lesson',
                   'type', 'submitted_by']


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sertificate
        fields = '__all__'

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
