from http import HTTPStatus
from random import randrange

import pytest

from tests.utils.base_classes.course_obj import CourseObject
from tests.utils.base_classes.course_tester import CourseTester
from tests.utils.constants import QUANTITY_COURSES_FOR_GET_LIST, FILTER_TYPES, STUDENTS_COUNT
from tests.utils.helpers import url_build, create_and_get_students_ids


@pytest.mark.django_db
def test_get_list_courses(api_client, courses_factory):
    created_courses = courses_factory(_quantity=QUANTITY_COURSES_FOR_GET_LIST)
    url = url_build('courses-list')
    course_tester = CourseTester(api_client)
    course_tester \
        .get_courses(url) \
        .validate_status_code(HTTPStatus.OK) \
        .is_equal(created_courses)


@pytest.mark.django_db
def test_get_course(api_client, courses_factory):
    created_course = courses_factory()
    url = url_build('courses-detail', kwargs={'pk': created_course.pk})
    course_tester = CourseTester(api_client)
    course_tester \
        .get_courses(url) \
        .validate_status_code(HTTPStatus.OK) \
        .is_equal(created_course)


@pytest.mark.django_db
@pytest.mark.parametrize('filter_type', FILTER_TYPES)
def test_courses_filter(api_client, courses_factory, filter_type):
    random_course = courses_factory(_quantity=QUANTITY_COURSES_FOR_GET_LIST)[
        randrange(0, QUANTITY_COURSES_FOR_GET_LIST)]
    url = url_build('courses-list', get_params={filter_type: getattr(random_course, filter_type)})
    course_tester = CourseTester(api_client)
    course_tester \
        .get_courses(url) \
        .validate_status_code(HTTPStatus.OK) \
        .is_equal([random_course])


@pytest.mark.django_db
def test_create_course(students_factory, api_client):
    course = CourseObject(name='Hello World')
    url = url_build('courses-list')
    course_tester = CourseTester(api_client)
    course_tester \
        .create_course(url, course) \
        .validate_status_code(HTTPStatus.CREATED) \
        .is_created()


@pytest.mark.django_db
@pytest.mark.parametrize('students_count', STUDENTS_COUNT)
def test_update_course(courses_factory, students_factory, api_client, students_count):
    course = courses_factory()
    students_ids = create_and_get_students_ids(students_factory, students_count)
    new_course_data = CourseObject(name='New name for a course', students=students_ids)
    url = url_build('courses-detail', kwargs={'pk': course.pk})
    course_tester = CourseTester(api_client)
    course_tester \
        .update_course(url, new_course_data) \
        .validate_status_code(HTTPStatus.OK) \
        .is_updated()


@pytest.mark.django_db
def test_remove_course(courses_factory, api_client):
    course = courses_factory()
    url = url_build('courses-detail', kwargs={'pk': course.pk})
    course_tester = CourseTester(api_client)
    course_tester \
        .delete_course(url) \
        .validate_status_code(HTTPStatus.NO_CONTENT) \
        .is_deleted(course.pk)
