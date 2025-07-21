import graphene
from graphene_django import DjangoObjectType
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
        fields = ('id', 'name', 'password', 'role', 'username', 'staffID')

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
