# Create your views here.
from random import randint
from django.shortcuts import get_object_or_404, render
from django.views import generic
from examer.models import Course, Exam, ExamQuestion


class IndexView(generic.ListView):
    template_name = 'examer/index.html'
    context_object_name = 'courses'

    def get_queryset(self):
        """Return all courses"""
        return Course.objects.all()


class DetailView(generic.DetailView):
    model = Course
    template_name = 'examer/detail.html'

    def get_queryset(self):
        """Return all exams for this course"""
        return super(DetailView, self).get_queryset().filter(id=self.kwargs['pk'])


def RandomQuestionFromCourseView(request, pk):
    course = get_object_or_404(Course, pk=pk)
    exam = course.exam_set.filter(course_id=pk).order_by('?')[0]
    question = exam.examquestion_set.filter(exam_id=exam.id).order_by('?')[0]

    return render(request, 'examer/question.html', {'course': course, 'exam': exam, 'question': question})


def ShowQuestionView(request, course_id, exam_id, question_id):
    question = get_object_or_404(ExamQuestion, pk=question_id)
    exam = question.exam
    print exam.name
    course = exam.course

    return render(request, 'examer/question.html', {'course': course, 'exam': exam, 'question': question})
