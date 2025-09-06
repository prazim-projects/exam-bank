from django.db import models
from .utils import exam_file_path    
# Create your models here.

def upload_exam_to(instance, filename):
        return f'exams/{instance.exam.year}/{instance.exam.course}/{filename}'


class ExamFile(models.Model):
    exam = models.ForeignKey('fetenaArchive.Exam', on_delete=models.CASCADE, related_name='exam_file')
    file = models.FileField(upload_to=exam_file_path, max_length=100)
   

    def __str__(self):
        return f'{self.exam.title}-{self.file.name}'
