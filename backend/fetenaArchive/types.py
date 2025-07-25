# from graphene import relay, ObjectType
import graphene
from graphene_django import DjangoObjectType
# from graphene_django.filter import DjangoFilterConnectionField

from .models import *
from file_api.models import *

class DifficultyRatingType(DjangoObjectType):
    class Meta:
        model = DifficultyRating
        fields = "__all__"

class PeerReviewType(DjangoObjectType):
    class Meta:
        model = PeerReview
        fields = '__all__'

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'role', 'username', 'staffID', 'email')

class ExamFileType(DjangoObjectType):
    class Meta:
        model = ExamFile
        fields = "__all__"

class ExamType(DjangoObjectType):
    class Meta:
        model = Exam
        fields = '__all__'

        file = graphene.List(ExamFileType)

    def resolve_files(self, info):
        return self.files.all()
