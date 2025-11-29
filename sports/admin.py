from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Sport, Coach, Player


# ---------------- Sport ----------------
class SportAdmin(admin.ModelAdmin):
    # Columns to display in admin list view
    list_display = ('id', 'name', 'description')
    list_filter = ('name',)
    search_fields = ('name', 'description')


admin.site.register(Sport, SportAdmin)


# ---------------- Coach ----------------
class CoachAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact', 'sport_display')
    list_filter = ('sport',)
    search_fields = ('name', 'contact', 'sport__name')

    # custom method to show sport name instead of ID
    def sport_display(self, obj):
        return obj.sport.name if obj.sport else '-'
    sport_display.short_description = 'Sport'


admin.site.register(Coach, CoachAdmin)


# ---------------- Player ----------------
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_display', 'sport_display', 'jersey_number')
    list_filter = ('sport',)
    search_fields = ('student__name', 'sport__name', 'jersey_number')

    # custom method to show related names
    def student_display(self, obj):
        return obj.student.name if obj.student else '-'
    student_display.short_description = 'Student'

    def sport_display(self, obj):
        return obj.sport.name if obj.sport else '-'
    sport_display.short_description = 'Sport'


admin.site.register(Player, PlayerAdmin)
