from rest_framework import serializers

from students.models import Course
from django.conf import settings


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate_students(self, value):
        value_len = len(value)
        if value_len > settings.MAX_STUDENTS_PER_COURSE:
            raise serializers.ValidationError('Too many students per course')
        if self.instance:
            current_students_count = self.instance.students.count()
            if current_students_count + value_len > settings.MAX_STUDENTS_PER_COURSE:
                raise serializers.ValidationError('Too many students per course')

        return value
