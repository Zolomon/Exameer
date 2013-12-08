# Exameer

To run:

`python bootstrap.py`

This will delete the `database.db` if it exists, and then perform a `python manage.py syncdb` which will create the
database and then fill it with data specified in `bootstrap.py`.

# Design
Questions are stored in `examer/static/examer/images/courses/[course id]/[exams|solutions]/[exam id]/[problem id].png`

* `[course id]`, is a tag name, such as `fmaa01a2`.
* `[exams|solutions]`, there are two directories in each course directory, one for exam questions, and one for solutions if they exist.
* `[exam id]`, id for the current exam, such as `20130823`
* `[problem id]`, a number from 0-N, N == (number of questions on exam - 1).

Currently you can visit `0.0.0.0:8000/course/all/` to see a list of all courses. 

You can go to a random question for a specified course at `0.0.0.0:8000/course/1/random/random/`.

# Course list:

1.  eitf05 - web security
2.  edan40 - functional programming
3.  fmaa01a2 - calculus, part II

# TODO:
* [ ] Show the name of question in detail view
* [X] Add next/prev buttons


*Copyright:* I should probably delete the PNGs that I have extracted so far, 
since I am not sure if they are public domain or copyrighted by my university, 
Lunds Tekniska Högskola, Sweden.