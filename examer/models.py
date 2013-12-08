from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Exam(models.Model):
    course = models.ForeignKey(Course)

    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class ExamQuestion(models.Model):
    exam = models.ForeignKey(Exam)
    name = models.IntegerField()

    def __unicode__(self):
        return str(self.name)


class Tag(models.Model):
    question = models.ForeignKey(ExamQuestion)
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return str(self.name)

