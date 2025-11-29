from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import TeacherDetail, Teacher
# from .models import Teacher, Classroom, Subject
from .serializers import TeacherSerializer, ClassroomSerializer, SubjectSerializer
from django.db.models import Avg,Min,Max,Sum,Count


from rest_framework.viewsets import ModelViewSet
# from .models import TeacherDetail
from .serializers import TeacherDetailSerializer


# class TeacherAPI(APIView):
     # def get(self, request):
         # in models,subject parent la irunthu child class data access pandrathuku,so related name classrooms nu edukorom
         # classroom=Subject.objects.filter(classrooms__capacity=70)
         # all_data=SubjectSerializer(classroom,many=True).data
         # return Response(all_data)
     # def get(self, request):
        #in models,subject parent la irunthu child class data access pandrathuku,so related name classrooms nu edukorom
         # classroom=Subject.objects.annotate(subject_count=Count('classrooms'))
         # for i in classroom:
         #     print(i.subject_name,i.subject_count)
         # return Response()

    # 1)in models,classroom child class data access pandrathuku
    # def get(self, request):
    #     classroom = Classroom.objects.filter(subject__subject_name="English")
    #     all_data = ClassroomSerializer(classroom, many=True).data
    #     return Response(all_data)

    #2)in models,classroom child model la irunthu parent model ah access pandraom
     # def get(self, request):
     #     classroom = Classroom.objects.get(id=3)
     #     print(classroom.room_no)
     #     print(classroom.subject)
     #     return Response()




    # def get(self, request):
    #     First get the Subject instance
        # subject_instance = Subject.objects.get(subject_name="Tamil")
        #
        # Then assign it to classroom
        # classroom = Classroom(
        #     room_no="D-101",
        #     floor=4,
        #     capacity=70,
        #     subject=subject_instance  # assign instance
        # )
        # classroom.save()
        # return Response("new classrooms created")

    # def get(self,request):

        #this one method ORM query for new data create panna In DB
    #     new_student=Teacher(name="messi",age=33,email="messi@gmail.com",phone="9898989312")
    #     new_student.save()
    #     return Response('New Teacher created')


         #this is another method ORM query for new data create panna In DB
        # Teacher.objects.create(name="Shalini", age=37, email="shalini@gmail.com", phone="989898930")
        # return Response('New Teacher created')
      #above 2 methods namma request la irunthu data vangama,direct ah data pass pandrom to DB


    #this one get pandrom all data va teacher table
     # def get(self, request):
     #     all_student=Teacher.objects.all()  #id base panni
     #     serializer_data=TeacherSerializer(all_student,many=True).data
     #     return Response(serializer_data)


     #this one get pandrom id base panni and name field data va teacher table
     #and note get method use panni 1 data only fetch panna mudiyum,if duplicate data availble means through the error[MultipleObjectsReturned]
     #and if DB table la data not available means error throw pannnum

     # def get(self, request):
     #     all_student=Teacher.objects.get(name="john",age=40)
     #     serializer_data=TeacherSerializer(all_student).data
     #     return Response(serializer_data)

         # all_student = Teacher.objects.first() #table la first data filter panna use pannuvom
         # all_student = Teacher.objects.last()  #table la last data filter panna use pannuvom


     # def get(self, request):
         # all_student=Teacher.objects.all().order_by("name") #alpahepet abcd..nu filter pannum
         # all_student = Teacher.objects.all().order_by("age")  # asc age la sort pannum
         # all_student = Teacher.objects.all().order_by("-age")    #desc order la sort pannum chharacter also filter pannalam
         # serializer_data=TeacherSerializer(all_student,many=True).data
         # return Response(serializer_data)

     # aggregate function particular field ku min, max,sum,avg
     # def get(self, request):
         # data = Teacher.objects.aggregate(Avg("age"))   # age colum ku Avg value
         # data = Teacher.objects.aggregate(Min("age"))   #  age colum ku Avg value
         # data = Teacher.objects.aggregate(Max("age"))   # age colum ku Avg value
         # data = Teacher.objects.aggregate(Sum("age"))   # age colum ku Avg value
         # return Response(data)




     #now filter method based ORM query
     #multiple records filter pannikalam error varathu
     #and if [DB] table la data not available means error throw pannathu empty list [] output varum

     # def get(self, request):
         # all_student = Teacher.objects.filter(name="john",age="40")  #two john data la irunthu age base panni filter panniirukain
         # all_student = Teacher.objects.filter(name="john").exclude(age="40") #this one two john record la age 40 illama john 38 age record mattum filter pannuthu
         # all_student = Teacher.objects.filter(age__gte=35) # age 35 or above filter pannuthu
         # all_student = Teacher.objects.filter(age__lte=35) #age 35 or below filter pannuthu

         # age from 35 la irunthu 40 varikum filter pannum
         # all_student = Teacher.objects.filter(age__range=(35,40))

         #name and two name filter pandrathuku
         # all_student = Teacher.objects.filter(name__in=('john','charles'))
         # serializer_data = TeacherSerializer(all_student, many=True).data
         # return Response(serializer_data)


class TeacherDetailViewSet(ModelViewSet):
    queryset = TeacherDetail.objects.all()
    serializer_class = TeacherDetailSerializer
class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer