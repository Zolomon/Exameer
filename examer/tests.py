"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.core.urlresolvers import reverse

from django.test import TestCase
from examer.models import Course


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


def create_course(name, description):
    return Course.objects.create(name=name, description=description)


class CourseViewTests(TestCase):

    def test_index_view_with_no_course(self):
        """
        If no courses exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('examer:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No courses are available.")
        self.assertQuerysetEqual(response.context['courses'], [])

    def test_index_view_with_one_course(self):
        """
        All courses should be displayed on the index page.
        """
        create_course("FMAA01 A2", "A2 - Endimensionell Analys")
        response = self.client.get(reverse('examer:index'))
        self.assertQuerysetEqual(response.context['courses'],
                                 ['<Course: FMAA01 A2>'])

    def test_index_view_with_multiple_courses(self):
        """
        All courses should be displayed on the index page.
        """
        create_course("FMAA01 A1", "A1 - Endimensionell Analys")
        create_course("FMAA01 A2", "A2 - Endimensionell Analys")
        create_course("FMAA01 A3", "A3 - Endimensionell Analys")
        response = self.client.get(reverse('examer:index'))
        self.assertQuerysetEqual(response.context['courses'],
                                 ['<Course: FMAA01 A1>','<Course: FMAA01 A2>','<Course: FMAA01 A3>'])

