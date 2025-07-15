import graphene
from graphene_django import DjangoObjectType

from .models import *

class ExamType(DjangoObjectType):
    class Meta:
        model = Exam
        fields = '__all__'

class DifficultyRatingType(DjangoObjectType):
    class Meta:
        model = DifficultyRating
        fields = "__all__"


class Query(graphene.ObjectType):
    all_exams = graphene.List(ExamType)
    exam_by_year = graphene.Field(ExamType, year=graphene.Int(required=True))
    exams_by_title = graphene.Field(ExamType, title=graphene.String(required=True))
    exams_by_course = graphene.Field(ExamType, course=graphene.String(required=True))

    difficulty_rating_by_exam = graphene.Field(DifficultyRatingType, exam_id=graphene.Int(required=True))

    def resolve_all_exams(root, info):
        return Exam.objects.only("title", "course", "year", "id", "department", "upload_date").all()
    
    def resolve_exam_by_year(root, info, year):
        try:
            return Exam.objects.get(year=year)
        except Exam.DoesNotExist:
            return None
    
    def resolve_exam_by_course(root, info, course):
        try:
            return Exam.objects.get(course=course)
        except Exam.DoesNotExist:
            return None

    def resolve_difficulty_by_exam(root, info, exam_id):
        try:
            return DifficultyRating.objects.get(exam_id=exam_id)
        except DifficultyRating.DoesNotExist:
            return None
      

schema = graphene.Schema(query=Query)

