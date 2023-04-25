from django.conf import settings

QUANTITY_COURSES_FOR_GET_LIST = 10
FILTER_TYPES = ('id', 'name')
STUDENTS_COUNT = (0, 5, 10, settings.MAX_STUDENTS_PER_COURSE, settings.MAX_STUDENTS_PER_COURSE + 1)
