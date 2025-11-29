from django.urls import path
from .views import StudentAPI,CourseAPI,RankSheetView,course_list_create,course_update_delete_getById

urlpatterns = [
    path('details/', StudentAPI.as_view()),
    path('details/<int:student_id>/', StudentAPI.as_view()),

    # Course API
    path('courses/', CourseAPI.as_view()),                    # GET all / POST new
    path('courses/<int:course_id>/', CourseAPI.as_view()),    # GET/PUT/PATCH/DELETE single course
    #RankAPi
    path('rank/', RankSheetView.as_view()),
    path('rank/<int:id>/', RankSheetView.as_view()),
    #function base api for course
    path('course/list/create/',course_list_create),
    path('course/update/delete/get/<int:course_id>/',course_update_delete_getById)


]
