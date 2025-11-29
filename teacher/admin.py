from django.contrib import admin
from .models import Teacher, Subject, Classroom, TeacherDetail


# Register your model with admin
class TeacherAdmin(admin.ModelAdmin):
    # Columns to display in admin list view
    list_display = ('id', 'name', 'age', 'email', 'phone')
    list_filter = ('age',)   # Filter sidebar (optional)
    search_fields = ('name', 'email', 'phone') # Search box fields
# Register the model
admin.site.register(Teacher, TeacherAdmin)

# ---------------- Subject ----------------
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject_name', 'code')
    list_filter = ('subject_name',)
    search_fields = ('subject_name', 'code')

admin.site.register(Subject, SubjectAdmin)
# ---------------- Classroom ----------------
class ClassroomAdmin(admin.ModelAdmin):
    # show ForeignKey in list_display
    list_display = ('id', 'room_no', 'floor', 'capacity', 'subject_display')
    list_filter = ('floor', 'subject')  # filter by subject also
    search_fields = ('room_no', 'subject__subject_name')  # search using subject name

    # custom method to display subject name instead of ID
    def subject_display(self, obj):
        return obj.subject.subject_name if obj.subject else '-'
    subject_display.short_description = 'Subject'

admin.site.register(Classroom, ClassroomAdmin)


# ---------------- TeacherDetail ----------------
class TeacherDetailAdmin(admin.ModelAdmin):
    # Show Teacher name directly in list view
    list_display = ('id', 'teacher', 'qualification', 'experience')
    search_fields = ('teacher__name', 'qualification')
admin.site.register(TeacherDetail, TeacherDetailAdmin)

