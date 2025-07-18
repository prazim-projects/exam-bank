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

class PeerReviewType(DjangoObjectType):
    class Meta:
        model = PeerReview
        fields = '__all__'


class Query(graphene.ObjectType):
    all_exams = graphene.List(ExamType)
    exam_by_year = graphene.Field(ExamType, year=graphene.Int(required=True))
    exam_by_title = graphene.List(ExamType, title=graphene.String(required=True))
    exam_by_course = graphene.List(ExamType, course=graphene.String(required=True))

    difficulty_rating = graphene.List(DifficultyRatingType)
    difficulty_rating_by_exam = graphene.List(DifficultyRatingType, exam_id=graphene.Int(required=True))

    peer_review_by_id = graphene.List(PeerReviewType, exam_id=graphene.Int(required=True))

    def resolve_all_exams(root, info):
        return Exam.objects.only("title", "course", "year", "id", "department", "upload_date").all()
    
    def resolve_difficulty_rating(root, info):
        return DifficultyRating.objects.only("difficulty_score", "rated_at", "rated_by").all()

    def resolve_exam_by_year(root, info, year):
        try:
            return Exam.objects.get(year=year)
        except Exam.DoesNotExist:
            return None
    
    def resolve_exam_by_course(root, info, course):
        
        print("QUERY RECIEVED: ", course)
        return Exam.objects.filter(course_iexact=course)
        
    def resolve_exam_by_title(root, info, title):
        try:
            return Exam.objects.filter(title=title)
        except Exam.DoesNotExist:
            return None
   

    def resolve_difficulty_rating_by_exam(root, info, exam_id):
        try:
            return DifficultyRating.objects.filter(exam_id=exam_id)
        except DifficultyRating.DoesNotExist:
            return None
      

    def resolve_peer_review_by_id(root, info, exam_id):
        try:
            return PeerReview.objects.filter(examID=exam_id)
        except PeerReview.DoesNotExist:
            return None
schema = graphene.Schema(query=Query)

