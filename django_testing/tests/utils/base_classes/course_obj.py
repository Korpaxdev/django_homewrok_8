from dataclasses import dataclass


@dataclass(frozen=True)
class CourseObject:
    name: None | str = None
    students: None | list[int] = None

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None}
