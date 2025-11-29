from django.core.serializers import serialize
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student, Course, RankSheet
from .serializers import CourseSerializer,RankSheetSerializer,Course_Data_Serializer,StudentSerializer,Student_Course_Serializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated



class StudentAPI(APIView):
    # permission_classes = [IsAuthenticated]

    # CREATE
    def post(self, request):
        print(request.data)
        new_student = Student(
            name=request.data["name"],
            dob=request.data["dob"],
            age=request.data["age"],
            email=request.data["email"],
            phone=request.data["phone"]
        )
        new_student.save()
        return Response("New student created", status=status.HTTP_201_CREATED)

    # READ (all or single student)
    def get(self, request, student_id=None):
        if student_id:  # Single student
            try:
                student = Student.objects.get(id=student_id)
                stud_dict = {
                    "id": student.id,
                    "name": student.name,
                    "dob": student.dob,
                    "age": student.age,
                    "email": student.email,
                    "phone": student.phone
                }
                return Response(stud_dict, status=status.HTTP_200_OK)
            except Student.DoesNotExist:
                return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        else:  # All students
            all_students=Student.objects.all()
            student_data=Student_Course_Serializer(all_students,many=True).data
            return Response(student_data)
            # get_students = Student.objects.all()
            # stud_list = []
            # for i in get_students:
            #     stud_dict = {
            #         "id": i.id,
            #         "name": i.name,
            #         "dob": i.dob,
            #         "age": i.age,
            #         "email": i.email,
            #         "phone": i.phone
            #     }
            #     stud_list.append(stud_dict)
            # return Response(stud_list, status=status.HTTP_200_OK)

    # def patch(self,request,student_id):
    #     student_data=Student.objects.filter(id=student_id)
    #     print(student_data)
    #     student_data.update(name=request.data["name"],
    #                         dob=request.data["dob"],
    #                         age=request.data["age"],
    #                         email=request.data["email"],
    #                         phone=request.data["phone"])
    #     print(student_data)
    #     return Response("student data updated")
        # PUT → full update (all fields required)
    def put(self, request, student_id):
        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"})


        student.name = request.data.get("name")
        student.dob = request.data.get("dob")
        student.age = request.data.get("age")
        student.email = request.data.get("email")
        student.phone = request.data.get("phone")
        student.save()

        return Response({"message": "Student data fully updated"})

    # PATCH → partial update (only given fields update)
    def patch(self, request, student_id):
        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"})

        # only available fields updated
        if "name" in request.data:
            student.name = request.data["name"]
        if "dob" in request.data:
            student.dob = request.data["dob"]
        if "age" in request.data:
            student.age = request.data["age"]
        if "email" in request.data:
            student.email = request.data["email"]
        if "phone" in request.data:
            student.phone = request.data["phone"]

        student.save()
        return Response({"message": "Student data partially updated"})

    # DELETE method
    def delete(self, request, student_id):

        student = Student.objects.get(id=student_id)
        student.delete()
        return Response({"message": "Student deleted successfully"})
#using modelserialize in CRUD operation
class CourseAPI(APIView):

    # POST → Create course
    def post(self, request):
        student_id = request.data.get('student')  # get the id
        course_name = request.data.get('course_name')
        description = request.data.get('description')

        # get Student object
        try:
            student_obj = Student.objects.get(id=student_id) if student_id else None
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=400)

        new_course = Course(
            student=student_obj,  # <-- pass object, not id
            course_name=course_name,
            description=description
        )
        new_course.save()
        return Response({"message": "Course created"})

        # serializer = CourseSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response({"message": "Course created", "data": serializer.data}, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # GET → List all courses or single course by ID
    def get(self, request, course_id=None):
        if course_id:  # If ID provided → fetch single course
            try:
                course = Course.objects.get(id=course_id)
                serializer = Course_Data_Serializer(course)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Course.DoesNotExist:
                return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
        else:  # If no ID → list all courses
            courses = Course.objects.all()
            serializer = Course_Data_Serializer(courses, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    # PUT → Full update
    def put(self, request, course_id):
        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Course fully updated", "data": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PATCH → Partial update
    def patch(self, request, course_id):
        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CourseSerializer(course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Course partially updated", "data": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE → Delete course
    def delete(self, request, course_id):
        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
        course.delete()
        return Response({"message": "Course deleted successfully"}, status=status.HTTP_200_OK)

#logical operation here post method manual and remaining method serialize
class RankSheetView(APIView):
    def post(self,request):
        total_marks =request.data["sub1"] + request.data["sub2"] + request.data["sub3"] +request.data["sub4"] + request.data["sub5"]

        average_marks=total_marks/5
        if (request.data["sub1"]>=35)and (request.data["sub2"] >=35) and (request.data["sub3"]>=35) and (request.data["sub4"]>=35) and (request.data["sub5"]>=35):
            student_result=True
        else:
            student_result=False
        new_data=RankSheet(sub1=request.data["sub1"],sub2=request.data["sub2"],
        sub3=request.data["sub3"],sub4=request.data["sub4"],sub5=request.data["sub5"],total=total_marks,average=average_marks,result=student_result)
        new_data.save()
        return Response("Data Saved")

    def get(self, request, id=None):
        if id is None:  # All data fetch
            all_data = RankSheet.objects.all()
            rank = RankSheetSerializer(all_data, many=True)
            return Response({"message": "All Data fetched", "data": rank.data})
        else:  # Particular id fetch
            try:
                data = RankSheet.objects.get(id=id)
                rank = RankSheetSerializer(data)
                return Response({"message": "Particular Data fetched", "data": rank.data})
            except RankSheet.DoesNotExist:
                return Response({"error": "Record not found"}, status=404)

    def put(self,request,id):
        rank_data=RankSheet.objects.filter(id=id)
        total_marks = request.data["sub1"] + request.data["sub2"] + request.data["sub3"] + request.data["sub4"] + \
                      request.data["sub5"]

        average_marks = total_marks / 5
        if (request.data["sub1"] >= 35) and (request.data["sub2"] >= 35) and (request.data["sub3"] >= 35) and (
                request.data["sub4"] >= 35) and (request.data["sub5"] >= 35):
            student_result = True
        else:
            student_result = False

        rank_data.update(sub1=request.data["sub1"], sub2=request.data["sub2"],
                             sub3=request.data["sub3"], sub4=request.data["sub4"], sub5=request.data["sub5"],
                             total=total_marks, average=average_marks, result=student_result)
        return Response('data updated')


# PUT → full update
#     def put(self, request, id):
#         try:
#             data = RankSheet.objects.get(id=id)
#         except RankSheet.DoesNotExist:
#             return Response({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)
#
#         update = RankSheetSerializer(data, data=request.data)  # full update
#         if update.is_valid():
#             update.save()
#             return Response({"msg": "Data fully updated", "data": update.data}, status=status.HTTP_200_OK)
#         return Response(update.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     PATCH → partial update
    # def patch(self, request, id):
    #     try:
    #         data = RankSheet.objects.get(id=id)
    #     except RankSheet.DoesNotExist:
    #         return Response({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)
    #
    #     update = RankSheetSerializer(data, data=request.data, partial=True)  # partial update
    #     if update.is_valid():
    #         update.save()
    #         return Response({"msg": "Data partially updated", "data": update.data}, status=status.HTTP_200_OK)
    #     return Response(update.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE → delete record
    def delete(self, request, id=None):
        try:
            data = RankSheet.objects.get(id=id)
        except RankSheet.DoesNotExist:
            return Response({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)

        data.delete()
        return Response({"msg": "Data deleted successfully"}, status=status.HTTP_200_OK)

#function base API
@api_view(['GET', 'POST'])
def course_list_create(request):
    # POST → Create new course
    if request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Course created", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # GET → Fetch all courses
    elif request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(
            {"message": "All Courses fetched", "data": serializer.data},
            status=status.HTTP_200_OK
        )

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def course_update_delete_getById(request, course_id):
    """
    GET -- fetch single course by id
    PUT -- full update (all fields required)
    PATCH -- partial update (only provided fields)
    DELETE -- delete record
    """
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

    # GET -> return single course
    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # PUT -> full update (all fields required)
    if request.method == 'PUT':
        serializer = CourseSerializer(course, data=request.data)  # full update
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Course fully updated", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PATCH -> partial update
    if request.method == 'PATCH':
        serializer = CourseSerializer(course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Course partially updated", "data": serializer.data},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE -> delete record
    if request.method == 'DELETE':
        course.delete()
        return Response({"message": "Course deleted successfully"}, status=status.HTTP_200_OK)


