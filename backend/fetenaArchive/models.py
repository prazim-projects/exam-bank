import uuid
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from file_api.models import *
from django.contrib.auth.models import User

class User(AbstractUser):
    role_choice = (
        ('student', 'Student'),
        ('department', 'Department'),
        ('college', 'college')
    )

    College = models.CharField("College", max_length=50, null=True, blank=True)
    organization_email = models.EmailField("Organization Email", max_length=254, default='test@etdu.et')
    role = models.CharField(max_length=10, choices=role_choice)
    staffID = models.CharField("given by organization", max_length=50, blank=True) 
    studentID = models.CharField(max_length=50, blank=True)
    
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
    # exam_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(choices=exam_type, max_length=10, default='TEST')
    year = models.IntegerField("Year exam was given")
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey('Exam_courses', on_delete=models.CASCADE, related_name='exams')
    upload_date = models.DateField(auto_now_add=True)
    visibility = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT)
    # exam_file = models.OneToOneField(ExamFile, on_delete=models.CASCADE, null=True)

    
    def __str__(self):
        return f'{self.year} - {self.course.name} - {self.get_title_display()}' 
    

class Exam_courses(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, null=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, related_name='Exam_courses')
    slug = models.SlugField(unique=True, blank=True, null=True)
    
    def save(self, *args, **kwargs):

        if not self.slug:
            if self.name:
                self.slug = slugify(self.name)
            else:
                self.slug = str(uuid.uuid4())[:8] # Use a short unique ID

        # Ensure the final slug is unique before saving
        original_slug = self.slug
        counter = 1
        while Exam_courses.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            self.slug = f'{original_slug}-{counter}'
            counter += 1

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.code} - {self.name}'


class Site(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    college = models.ManyToManyField('College', related_name='sites', blank=True)

    def __str__(self):
        return self.name



class College(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    departments = models.ForeignKey('Department', on_delete=models.CASCADE, related_name='colleges', null=True, blank=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='colleges')
    authorized_users = models.ManyToManyField(User,
        related_name='authorized_college',
        blank=True,
        help_text="Users authorized and part of college staff."
    )

    def __str__(self):
        return self.name

    
class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    head_of_department = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    courses = models.ManyToManyField('Exam_courses', related_name='departments', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    staff = models.ManyToManyField(User, related_name='department_staff', blank=True)
    authorized_users = models.ManyToManyField(User,
        related_name='authorized_departments',
        blank=True,
        help_text="Users authorized and acknowledged by the department."
    )

    def __str__(self):
        return self.name

class DifficultyRating(models.Model):
    stars = (
        (1, 'VERY EASY'),
        (2, 'EASY'),
        (3, 'MODERATE'),
        (4, 'HARD'),
        (5, 'VERY HARD'),
    )
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    rated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    difficulty_score = models.IntegerField(choices=stars)
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
    