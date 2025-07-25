from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from file_api.models import *
# Create your models here.

class User(AbstractUser):
    role_choice = (
        ('student', 'Student'),
        ('lecturer', 'Lecturer'),
        ('staff', 'Staff')
    )
    organization_email = models.EmailField("Organization Email", max_length=254, default='test@etdu.et')
    role = models.CharField(max_length=10, choices=role_choice)
    staffID = models.CharField("given by organization", max_length=50, default='ETDU/20067/staff') 
    studentID = models.CharField(max_length=50, default='ETDU/29090/15')
    
    def __str__(self):
        return self.username


class Exam(models.Model):
    class Status(models.TextChoices):
        DRAFT =  'Draft'
        PUBLISHED = 'Published'
        ARCHIVED =  'Archived'

    exam_type = (
        ('final', 'Final'),
        ('mid', 'Mid'),
        ('quiz', 'Quiz'),
    )

    title = models.CharField(choices=exam_type, max_length=10, default='TEST')
    year = models.IntegerField("Year exam was given")
    course = models.CharField("course_name", max_length=50)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.JSONField("Departments course is given")
    upload_date = models.DateField(auto_now_add=True)
    visibility = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT)
    # exam_file = models.ForeignKey(ExamFile, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.year} - {self.course} - {self.get_title_display()}' 
    
class DifficultyRating(models.Model):
    stars = (
        ('1', 'VERY EASY'),
        ('2', 'EASY'),
        ('3', 'MODERATE'),
        ('4', 'HARD'),
        ('5', 'VERY HARD'),
    )
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    rated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    difficulty_score = models.CharField(choices=stars, max_length=2)
    rated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.get_difficulty_score_display()}'
    

class PeerReview(models.Model):

    reviewerID = models.ForeignKey(User, on_delete=models.CASCADE)
    examID = models.ForeignKey(Exam, on_delete=models.CASCADE)
    review_text = models.CharField(max_length=120)
    reviewed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.reviewerID}'
    