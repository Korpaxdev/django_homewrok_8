from dataclasses import dataclass


@dataclass(frozen=True)
class BaseErrorMessages:
    WRONG_STATUS_CODE = 'Status code is not equal.\nExpected: %s\nActual: %s\nResponse: %s'
    NOT_EQUAL_COURSES = 'Courses and data are not equal.\nData: %s\nCourses: %s'
    COURSE_IS_NOT_DELETED = 'Course is not deleted.\nExpected: %s\nActual: %s'
