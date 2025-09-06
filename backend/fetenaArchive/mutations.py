import graphene
from graphene_file_upload.scalars import Upload
from file_api.utils import exam_file_path
from .types import *
from . import models
from django.contrib.auth import get_user_model
from graphql_jwt.shortcuts import create_refresh_token, get_token
from django.db import transaction

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
    def mutate(cls, root, info, title, year, course, uploadedBy, visibility, file ):    
        try:
            user_instance = User.objects.get(pk=uploadedBy)
            course_instance = Exam_courses.objects.get(name=course) 
    
            with transaction.atomic():
                new_exam = Exam.objects.create(title=title, year=year, course=course_instance, uploaded_by=user_instance, visibility=visibility)
                exam_file = ExamFile.objects.create(file=file, exam=new_exam)
               
            return createExamMutation(exam=new_exam, exam_file=exam_file)
        
        except Exam_courses.DoesNotExist:
            raise Exception(f"Error: A course with the name '{course_title}' was not found. Please check the spelling or create the course first.")
        except User.DoesNotExist:
            raise Exception(f"User with ID {uploader_id} not found.")
        except Exam_courses.DoesNotExist:
            raise Exception(f"Course with ID {course_title} not found.")
        except Exception as e:
            # Catch any other potential errors
            raise Exception(f"An error occurred: {e}")        



class createUserDept(graphene.Mutation):
    user = graphene.Field(UserType)
    token = graphene.String()
    refresh_token = graphene.String()

    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        role = graphene.String(required=True)
        staffID = graphene.String(required=True)
        
    @classmethod
    def mutate(cls, root, info, username, email, password, role, staffID=None):
        user = get_user_model()(
            username=username,
            password=password,
        )
        role = role.lower()

        if role not in ['staff', 'department']:
            raise Exception("Invalid role. Must be 'staff' or 'department'.")

        user = models.User(username=username, email=email, role=role)

        if role == 'college':
            if not staffID:
                raise Exception("staffID is required for staff role.")
            user.staffID = staffID
            user.isStaff = True

        elif role == 'department':
            user.isDepartment = True

        user.set_password(password)
        user.save()
        token = get_token(user)
        refresh_token = create_refresh_token(user)

        return createUserDept(user=user, token=token, refresh_token=refresh_token)


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

        if role not in ['college', 'student', 'department']:
            raise Exception("Invalid role. Must be 'college' or 'student' or 'department'.")

        user = models.User(username=username, email=email, role=role)

        if role == 'college':
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
        