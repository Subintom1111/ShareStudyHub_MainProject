from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .models import Thread, ChatMessage


 
class CustomUserAdmin(UserAdmin):

   def get_queryset(self, request):
        return User.objects.exclude(is_superuser=True)


admin.site.register(User,CustomUserAdmin),
admin.site.register(Profile),
admin.site.register(Profilete),
admin.site.register(Courses),
admin.site.register(Feedback),
admin.site.register(ExamMark),
admin.site.register(Assignment),
admin.site.register(Submission),
admin.site.register(Notification),
admin.site.register(CourseNotes),
admin.site.register(Product),
admin.site.register(DeliveryAddress),
admin.site.register(ChatMessage),


class ChatMessage(admin.TabularInline):
    model = ChatMessage


class ThreadAdmin(admin.ModelAdmin):
    inlines = [ChatMessage]
    class Meta:
        model = Thread


admin.site.register(Thread, ThreadAdmin)


