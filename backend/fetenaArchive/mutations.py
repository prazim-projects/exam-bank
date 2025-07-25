import graphene
from graphene_file_upload.scalars import Upload
from file_api.utils import exam_file_path
from .types import UserType
from . import models

class UploadExamMutation(graphene.Mutation):
    class Arguments:
        file = Upload(required=True)

    success = graphene.Boolean()

    def mutate(Self, info, file, **kwargs):
        file.save(exam_file_path)
        return UploadFileMutation(success=True)

class createExamMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        year = graphene.Int(required=True)
        course = graphene.String(required=True)
        uploadedBy = graphene.String(required=True)
        visibility = graphene.String(required=False)
    
    @classmethod
    def mutate(cls, root, info,title, year, course, uploadedBy, visibility ):
        exam = models.Exam(title=title, year=year, uploadedBy=uploadedBy, visibility=visibiltiy)
        return exam

class createUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        role = graphene.String(required=True)
        studentID = graphene.String(required=False)
        staffID = graphene.String(required=False)
    
    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, username, email, password, role, staffID=None, studentID=None):
        user = models.User(username=username, email=email, role=role)
        role = role.lower()

        if role not in ['staff', 'student']:
            raise Exception("Invalid role. Must be 'staff' or 'student'.")

        user = models.User(username=username, email=email, role=role)

        if role == 'staff':
            if not staffID:
                raise Exception("staffID is required for staff role.")
            user.staffID = staffID

        elif role == 'student':
            if not studentID:
                raise Exception("studentID is required for student role.")
            user.studentID = studentID

        user.set_password(password)
        user.save()

        return createUser(user=user)
        