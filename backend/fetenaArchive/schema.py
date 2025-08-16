import graphene
import graphql_jwt
from graphql_jwt.decorators import login_required

from graphene_django import DjangoObjectType

from .mutations import *
from file_api.models import *
from .types import *


class Query(graphene.ObjectType):
    all_exams = graphene.List(ExamType, limit=graphene.Int(required=False), offset=graphene.Int(required=False))
    exam_by_year = graphene.Field(ExamType, year=graphene.Int(required=True))
    exam_by_title = graphene.List(ExamType, title=graphene.String(required=True))
    exam_by_course = graphene.List(ExamType, course=graphene.String(required=True))
    exam_by_visibility = graphene.List(ExamType, visibility=graphene.String(required=True), limit=graphene.Int(required=False), offset=graphene.Int(required=False))

    difficulty_rating = graphene.List(DifficultyRatingType)
    difficulty_rating_by_exam = graphene.List(DifficultyRatingType, exam_id=graphene.Int(required=True))

    peer_review_by_id = graphene.List(PeerReviewType, exam_id=graphene.Int(required=True))

    user_by_id = graphene.Field(UserType, id=graphene.String())
    files = graphene.List(ExamFileType)

    # exam = relay.ConnectionField(examConnection)
    # all_exams = DjangoFilterConnectionField(examFilterNode)
 
    # def resolve_exam(root, info, **kwargs):
    #     return Exam.objects.all()
    
    @login_required
    def resolve_all_exams(root, info, limit=None, offset=None):
        examQuery = Exam.objects.all()
        if offset:
            examQuery = examQuery[offset:]
        if limit:
            examQuery = examQuery[:limit]
        
        return examQuery

    @login_required   
    def resolve_difficulty_rating(root, info):
        return DifficultyRating.objects.only("difficulty_score", "rated_at", "rated_by").all()

    @login_required
    def resolve_exam_by_year(root, info, year):
        try:
            return Exam.objects.get(year=year)
        except Exam.DoesNotExist:
            return None
    @login_required
    def resolve_exam_by_course(root, info, course):
        
        print("QUERY RECIEVED: ", course)
        return Exam.objects.filter(course=course)
    
    @login_required
    def resolve_exam_by_title(root, info, title):
        try:
            return Exam.objects.filter(title=title)
        except Exam.DoesNotExist:
            return None

    def resolve_exam_by_visibility(root, info, visibility, limit, offset):
        examV = Exam.objects.filter(visibility=visibility)
        if offset:
            examV = examV[offset:]
        if limit:
            examV = examV[:limit]
      
        return examV

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

    @login_required
    def resolve_user_by_id(root, info, id):
        return User.objects.get(pk=id)

    def resolve_files(root, info):
        return ExamFile.objects.select_related('exam').all()


class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
    user = graphene.Field(UserType)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        return cls(user=info.context.user)

class Mutation(graphene.ObjectType):
    token_auth = ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

    upload_file = UploadExamMutation.Field()
    create_user = createUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

