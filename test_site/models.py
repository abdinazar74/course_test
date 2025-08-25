from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

class UserProfile(AbstractUser):
    ROLE_CHOICES = (
    ('admin', 'admin'),
    ('teacher', 'teacher'),
    ('student', 'student')
    )
    role = models.CharField(max_length=100, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

class Strike(models.Model):
    student = models.ForeignKey(UserProfile, related_name="strikes",on_delete=models.CASCADE)
    date = models.DateField()
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('student', 'date')
        ordering = ['-date']


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    LEVEL_CHOICES = (
    ('beginner', 'beginner'),
    ('elementary', 'elementary'),
    ('intermediate', 'intermediate')
    )
    level = models.CharField(max_length=100, choices=LEVEL_CHOICES, default='beginner')
    price = models.DecimalField(decimal_places=2, max_digits=10)
    video = models.URLField()
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.course_name

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    video_url = models.URLField()
    content = models.TextField()
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Assingment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    LEVEL_CHOICES = (
    ('beginner', 'beginner'),
    ('pre_intermediate', 'pre_intermediate'),
    ('upper_intermediate', 'upper_intermediate')
    )
    level = models.CharField(max_length=100, choices=LEVEL_CHOICES, default='beginner')
    due_date = models.DateTimeField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    TYPE_CHOICES = (
    ('text', 'text'),
    ('test', 'test'),
    ('exam', 'exam')
    )
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    submitted_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

class Exam(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    questions = models.CharField(max_length=200)
    passing_score = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title

class Sertificate(models.Model):
    student_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateTimeField()
    certificate_url = models.URLField()

class Review(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, related_name='reviews', on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(0, 6)])
    comment = models.TextField()











