from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from LearnHub.serializers import Userserializers,CategorySerializer,CourseSerializer,EnrollmentSerializer
from LearnHub.models import CategoryDb, CourseDb,EnrollmentDb
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class SignupView(APIView):
    def post(self,request):
        form_data = request.data
        serializer_instance = Userserializers(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({"message":"User Created Successfully"},status=201)
        else:
            return Response({"message":"Invalid data provided"},status=400)

class userlistview(APIView):
    def get(self,request):
        users = User.objects.all()
        serializer_instance = Userserializers(users,many=True)
        return Response(serializer_instance.data,status=200)

class CategoryListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        category = CategoryDb.objects.filter(user=request.user)
        serializer_instance = CategorySerializer(category,many=True)
        return Response(serializer_instance.data)

    def post(self,request):
        serializer_instance=CategorySerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save(user=request.user)
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

class CategoryUpdateDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,category_id):
        qs = get_object_or_404(CategoryDb,id = category_id,user=request.user)
        serializer_instance=CategorySerializer(qs)
        return Response(serializer_instance.data)

    def put(self,request,category_id):
        category = get_object_or_404(CategoryDb,id=category_id,user=request.user)
        serializer_instance = CategorySerializer(data=request.data,instance=category)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

    def delete(self,request,category_id):
        qs = get_object_or_404(CategoryDb,id=category_id,user=request.user)
        qs.delete()
        return Response({
            "Message": "Deleted SuccessFully"
        })

class CourseCreateListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        course = CourseDb.objects.filter(user=request.user)
        serializer_instance = CourseSerializer(course,many=True)
        return Response(serializer_instance.data)

    def post(self,request):
        serializer_instance= CourseSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save(user=request.user)
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

class CourseRetrieveUpdateDeleteView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request,course_id):
        qs = get_object_or_404(CourseDb,id=course_id,user=request.user)
        serializer_instance = CourseSerializer(qs)
        return Response(serializer_instance.data)

    def put(self,request,course_id):
        course = get_object_or_404(CourseDb,id=course_id,user=request.user)
        serializer_instance = CourseSerializer(data=request.data,instance=course)
        if serializer_instance.is_valid():
            serializer_instance.save(user=request.user)
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

    def delete(self,request,course_id):
         qs = get_object_or_404(CourseDb,id=course_id,user=request.user)
         qs.delete()
         return Response({
                "Message": "Deleted SuccessFully"
                })


class EnrollmentCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        course_id = request.data.get('course')

        course = get_object_or_404(CourseDb, id=course_id)

        # Check duplicate enrollment
        already_enrolled = EnrollmentDb.objects.filter(
            course=course,
            student=request.user
        ).exists()

        if already_enrolled:
            return Response({"message": "Already enrolled in this course"})

        serializer_instance = EnrollmentSerializer(data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save(
                student=request.user,
                course=course
            )
            return Response(serializer_instance.data)
        
        else:
            return Response(serializer_instance.errors)


    def get(self, request):
        qs = EnrollmentDb.objects.filter(student=request.user)
        serializer_instance = EnrollmentSerializer(qs, many=True)
        return Response(serializer_instance.data)

class EnrollmentRetrieveDelete(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,enrollment_id):
        qs = get_object_or_404(EnrollmentDb,id=enrollment_id,student = request.user)
        serializer_instance= EnrollmentSerializer(qs)
        return Response(serializer_instance.data)

    def delete(self,request,enrollment_id):
        qs = get_object_or_404(EnrollmentDb,id=enrollment_id,student=request.user)
        qs.delete()
        return Response({
            "message":"deleted successfully"
        })

        




