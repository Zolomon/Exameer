from django.conf.urls import patterns, include, url

from examer import views

urlpatterns = patterns('',
                       url(r'^all/$', views.IndexView.as_view(), name='index'),
                       url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
                       url(r'^(?P<pk>\d+)/random/random/$', views.RandomQuestionFromCourseView, name='random_question'),
                       url(r'^(?P<course_id>\d+)/(?P<exam_id>\d+)/(?P<question_id>\d+)/$', views.ShowQuestionView,
                           name='question'),
                       )