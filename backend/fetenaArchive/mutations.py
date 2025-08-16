import graphene
from graphene_file_upload.scalars import Upload
from file_api.utils import exam_file_path
from .types import *
from . import models
from django.contrib.auth import get_user_model
from graphql_jwt.shortcuts import create_refresh_token, get_token


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
        file = Upload(required=True)
    
    exam = graphene.Field(ExamType)
    exam_file = graphene.Field(ExamFileType)
    
    @classmethod
    def mutate(cls, root, info,title, year, course, uploadedBy, visibility, file ):
        with transaction.atomic():
            exam = models.Exam(title=title, year=year, uploadedBy=uploadedBy, visibility=visibiltiy)
            exam_file = ExamFile.objects.create(file=file, exam=exam)
        return exam

class createUser(graphene.Mutation):
    user = graphene.Field(UserType)
    token = graphene.String()
    refresh_token = graphene.String()

    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        role = graphene.String(required=True)
        studentID = graphene.String(required=False)
        staffID = graphene.String(required=False)
    
    @classmethod
    def mutate(cls, root, info, username, email, password, role, staffID=None, studentID=None):
        user = get_user_model()(
            username=username,
            password=password,
        )
        role = role.lower()

        if role not in ['staff', 'student', 'department']:
            raise Exception("Invalid role. Must be 'staff' or 'student' or 'department'.")

        user = models.User(username=username, email=email, role=role)

        if role == 'staff':
            if not staffID:
                raise Exception("staffID is required for staff role.")
            user.staffID = staffID
            user.isStaff = True

        elif role == 'student':
            if not studentID:
                raise Exception("studentID is required for student role.")
            user.studentID = studentID

        user.set_password(password)
        user.save()
        token = get_token(user)
        refresh_token = create_refresh_token(user)


        return createUser(user=user, token=token, refresh_token=refresh_token)
        