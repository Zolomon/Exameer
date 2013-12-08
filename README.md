# Exameer

To run:

`python bootstrap.py`

This will delete the `database.db` if it exists, and then perform a `python manage.py syncdb` which will create the
database and then fill it with data specified in `bootstrap.py`.

# Design
Questions are stored in examer/static/examer/images/courses/[course id]/[exams|solutions]/[exam id]/[problem id].png

* `[course id]`, is a tag name, such as `fmaa01a2`.
* `[exams|solutions]`, there are two directories in each course directory, one for exam questions, and one for solutions if they exist.
* `[exam id]`, id for the current exam, such as `20130823`
* `[problem id]`, a number from 0-N, N == (number of questions on exam - 1).

# TODO:
* [ ] Show the name of question in detail view
* [X] Add next/prev buttons
