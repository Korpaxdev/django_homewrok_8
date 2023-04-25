import urllib.parse as urllib_parse
from typing import Callable

from rest_framework.reverse import reverse


def url_build(url_name: str, **kwargs) -> str:
    """
    Build a URL with reverse.
    If kwargs has a get_params key then the function adds these params to the url as get params
    """
    get_params = kwargs.pop('get_params', None)
    url = reverse(url_name, **kwargs)
    if get_params:
        url += f"?{urllib_parse.urlencode(get_params)}"
    return url


def create_and_get_students_ids(factory: Callable, count: int):
    """
    Create students with factory and return their id
    if count is 0 then return empty list
    """
    students_ids = []
    if count:
        students = factory(_quantity=count)
        students_ids = [s.pk for s in students]
    return students_ids
