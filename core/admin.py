from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from core.forms import SignUpForm
from core.models import NewsFeeds, reminder, Profile


class NewsFeedsAdmin(admin.ModelAdmin):
    list_display = ('id','created','message','image',)

admin.site.register(NewsFeeds, NewsFeedsAdmin)

class reminderAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'event',)
admin.site.register(reminder, reminderAdmin)

# class reminderAdmin(admin.ModelAdmin):
#     list_display = ('id', 'date', 'event',)
#
# class CustomUserAdmin(ModelAdmin):
#     form = SignUpForm
#
# admin.site.register(SignUpForm, CustomUserAdmin)

