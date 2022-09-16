import pytest

from tests.conftest import create_user
from users.forms import UserCreateForm


def test_user_form(db):
    data = {'username': 'test', 'email': 'test@mail.com', 'password': '11111111'}
    form = UserCreateForm(data=data)
    assert form.is_valid()
    assert form.username == 'test'
    assert form.email == 'test@mail.com'
