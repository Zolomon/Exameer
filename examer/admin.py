from django.contrib import admin
from examer.models import Course, Exam, ExamQuestion

admin.site.register(Course)
admin.site.register(Exam)
admin.site.register(ExamQuestion)