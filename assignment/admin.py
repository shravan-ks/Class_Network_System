from django.contrib import admin

# Register your models here.
from assignment.models import assignment, AssignmentAns


class AssignmentAnsAdmin(admin.ModelAdmin):
    list_display = ('Paper','user','Title','created',)

admin.site.register(AssignmentAns, AssignmentAnsAdmin)

class AssigmentAdmin(admin.ModelAdmin):
    list_display = ('dept','sem','Paper','title','sub', 'Attachments','From', )

admin.site.register(assignment, AssigmentAdmin)

