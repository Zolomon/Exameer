__author__ = 'bengt'

from django.conf import settings
from exameer import settings
import sys
import os
import sqlite3
from subprocess import call
print "Hello World"
import pexpect

#for x in os.walk("/home/bengt/code/python/exameer/examer/static/examer/images/courses"):
#    print x

try:
    os.remove('database.db')
except OSError:
    pass

print 'pexpecting..'
child = pexpect.spawn('python manage.py syncdb')
child.expect('Would you like to create one now.*')
child.sendline('yes')
child.expect('Username.*')
child.sendline()
child.expect('Email.*')
child.sendline()
child.expect('Password.*')
child.sendline('1234')
child.expect('Password.*')
child.sendline('1234')
print 'end of pexpecting..'

#courses = ["eitf05", "fmaa01a2"]

#courses = [
#    (
#        ('eitf05', "Web Security"),
#        ('exams', 'solutions'),
#        #[('091021', 14), ('101020', 14), ('111019', 14), ('121024', 14)]
#    ),
#
#    (
#        ('fmaa01a2', "Calculus - A2"),
#        ('exams', 'solutions'),
#        #[('20100823', 6)]
#    )
#]

con = sqlite3.connect('database.db')
cursor = con.cursor()

# This will rename all files by absolute path in the dir you specify.  REALLY NICE SCRIPT!!!
# ls -R . | awk '/:$/&&f{s=$0;f=0}/:$/&&!f{sub(/:$/,"");s=$0;f=1;next}NF&&f{ print s"/"$0 }' | rename -n 's/solution_\d+-\d+-\d+\.(\d+)\.png$/$1.png/'

path = "/home/bengt/code/python/exameer/examer/static/examer/images/courses"

## Insert courses
courses = [dirs for root, dirs, files in os.walk(path) if root == path][0]

for course in courses:

    course_description = ""
    course_name = course

    coursequery = ('INSERT INTO examer_course (name, description) VALUES (?, ?);', [course_name, ''])
    print course_name, coursequery

    cursor.execute('INSERT INTO examer_course (name, description) VALUES (?, ?);', [course_name, ''])
    cursor.execute("SELECT id FROM examer_course WHERE name=? LIMIT 1;", [course_name])
    course_id = cursor.fetchone()[0]

    # Get path to exams folder for this course
    pdf_types = path + '/' + course + '/'
    types = [dirs for root, dirs, files in os.walk(pdf_types) if root == pdf_types][0]
    type = types[0]

    exams_path = pdf_types + type + '/'
    exams = [dirs for root, dirs, files in os.walk(exams_path) if root == exams_path][0]

    # Iterate over the exam dirs in this course's exams folder
    for exam in exams:
        examquery = ('INSERT INTO examer_exam (course_id, name) VALUES (?, ?)', [course_id, exam])
        print exam, examquery

        cursor.execute('INSERT INTO examer_exam (course_id, name) VALUES (?, ?)', [course_id, exam])
        cursor.execute("SELECT id FROM examer_exam WHERE name=? LIMIT 1;", [exam])
        exam_id = cursor.fetchone()[0]

        exam_path = exams_path+exam+'/'

        # Iterate over each image in each exams folder
        images = [files for root, dirs, files in os.walk(exam_path) if root == exam_path][0]
        for image in images:
            imgquery = ('INSERT INTO examer_examquestion (exam_id, name) VALUES (?, ?)',
                           [exam_id, image.split('.')[0]])
            print imgquery
            cursor.execute('INSERT INTO examer_examquestion (exam_id, name) VALUES (?, ?)',
                           [exam_id, image.split('.')[0]])
            #image_path = exam_path + image
            #print '\t', image_path

con.commit()
con.close()






## Insert images


#for course in courses:
#    course_name = course[0]
#    course_dirs = course[1]
#    course_exams = course[2]
#    print course_name
#    cursor.execute('INSERT INTO examer_course (name, description) VALUES (?, ?);', [course_name[0], course_name[1]])
#    cursor.execute("SELECT id FROM examer_course WHERE name=? LIMIT 1;", [course_name[0]])
#    course_id = cursor.fetchone()[0]
#
#    for exam in course_exams:
#        cursor.execute('INSERT INTO examer_exam (course_id, name) VALUES (?, ?)', [course_id, exam[0]])
#        cursor.execute("SELECT id FROM examer_exam WHERE name=? LIMIT 1;", [exam[0]])
#        exam_id = cursor.fetchone()[0]
#
#        for question in range(exam[1]):
#            question_name = question+1
#            print course, course_name, exam, question_name
#            cursor.execute('INSERT INTO examer_examquestion (exam_id, name) VALUES (?, ?)', [exam_id, question_name])
#
#print "done ..."
#    #for dir in course_dirs:
#    #    cursor.execute('INSERT INTO mastery_exam (course_id)')

#con.commit()
#con.close()



