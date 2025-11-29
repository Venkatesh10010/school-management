from django.core.serializers import serialize
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle, ScopedRateThrottle
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, filters

from .pagination import LaptopCursorPagination
from .serializers import CourseSerializer, StudentSerializer
from.models import *
from.serializers import *
# from .throttles import LaptopGetThrottle


# from .throttles import  LaptopGetThrottle


class BookView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    # throttle_classes = [UserRateThrottle]
    # permission_classes = [AllowAny]
    # throttle_classes = [UserRateThrottle,AnonRateThrottle]  #this for check auth user and unauth user our setting.py file anno&user'for testing
    # throttle_classes = [BookPostThrottle]  # only POST limited to 1/day
    # throttle_scope = 'book_post'
    # throttle_classes = [ScopedRateThrottle]
    # throttle_scope = 'book_post'

    # permission_classes = [AllowAny]  # allow anonymous so AnonRateThrottle can apply
    # throttle_classes = [AnonRateThrottle]
    queryset=Book.objects.all()
    serializer_class = Book_Serializer

    # def get_queryset(self):
        # get tittle value from URL path
        # tittle = self.kwargs.get('tittle')
        # if tittle:
        #     return Book.objects.filter(tittle__iexact=tittle)  # exact match (case-insensitive)
        # return Book.objects.all()

    # def get_queryset(self):
    #     query param name = 'tittle' because your model field is named `tittle`
        # q = self.request.query_params.get('tittle', None)
        # if q:
        #     use case-insensitive contains so partial match works
            # return Book.objects.filter(tittle=q)
        # no filter -> return all
        # return Book.objects.all()


class LaptopView(generics.ListCreateAPIView):
    # def get_queryset(self):
    #     return Laptop.objects.filter(brand="HP")
    # def perform_create(self, serializer):
    #     serializer.save(user_type="high performance")
    permission_classes = [IsAuthenticated]
    # throttle_classes = [UserRateThrottle]

    #this one get method ku only restriction not any methods from class and throttles.py file code map panni iruakain
    # throttle_classes = [LaptopGetThrottle]  # only GET limited to 3/day And this class throttle.py file la map agiruku
    # throttle_classes = [ScopedRateThrottle]
    # throttle_scope = 'book_post'
    queryset=Laptop.objects.all()
    serializer_class = Laptop_Serializer

    # FILTER + SEARCH + ORDER support
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['brand', 'model_name']  # exact / field filters
    search_fields = ['brand', 'model_name']  # '^brand' => starts-with on brand, model_name partial
    # ordering_fields = ['brand', 'model_name','id']  # allow ordering by these fields
    # ordering = ['-id']  # default ordering (optional)
    # pagination_class = LaptopPagination   # enable pagination for this viewset
    # USE LIMIT-OFFSET PAGINATION
    # pagination_class = LaptopLimitOffsetPagination
    # Use Cursor pagination
    pagination_class = LaptopCursorPagination



class LaptopViewById(generics.RetrieveUpdateDestroyAPIView):
    # def perform_update(self, serializer):
    #     serializer.save(user_type="low performance")
    queryset = Laptop.objects.all()
    serializer_class = Laptop_Serializer

# Add these new viewsets (append to file)
class CourseView(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer