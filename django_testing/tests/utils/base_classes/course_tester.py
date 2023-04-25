from http import HTTPStatus

from rest_framework.test import APIClient

from students.models import Course
from students.serializers import CourseSerializer
from tests.utils.base_classes.course_obj import CourseObject
from tests.utils.error_messages import BaseErrorMessages


class CourseTester:
    def __init__(self, api_client: APIClient):
        self.response = None
        self.data = None
        self.client = api_client

    def get_courses(self, url):
        self.response = self.client.get(url)
        self.data = self.response.json()
        return self

    def create_course(self, url: str, course: CourseObject):
        self.response = self.client.post(url, data=course.to_dict())
        self.data = self.response.json()
        return self

    def update_course(self, url: str, update_data: CourseObject):
        self.response = self.client.patch(url, data=update_data.to_dict())
        self.data = self.response.json()
        return self

    def delete_course(self, url: str):
        self.response = self.client.delete(url)
        return self

    def validate_status_code(self, status_code: HTTPStatus):
        if self.response:
            assert self.response.status_code == status_code, BaseErrorMessages.WRONG_STATUS_CODE % (
                status_code.value, self.response.status_code, self.data)
        return self

    def is_equal(self, created_courses: list[Course] | Course):
        if self.data:
            if type(created_courses) == list:
                serialize_data = CourseSerializer(created_courses, many=True).data
                assert self.data == serialize_data, BaseErrorMessages.NOT_EQUAL_COURSES % (self.data, serialize_data)
            else:
                serialize_data = CourseSerializer(created_courses).data
                assert self.data == serialize_data, BaseErrorMessages.NOT_EQUAL_COURSES % (self.data, serialize_data)

    def is_created(self):
        if self.data:
            course_id = self.data.get('id')
            course_name = self.data.get('name')
            students = self.data.get('students')
            students_ids = tuple(students) if students else None

            Course.objects.get(id=course_id, name=course_name, students=students_ids)

    def is_updated(self):
        self.is_created()

    @staticmethod
    def is_deleted(deleted_course_id: int):
        course = Course.objects.filter(id=deleted_course_id)
        assert not course, BaseErrorMessages.COURSE_IS_NOT_DELETED % ([], course)
