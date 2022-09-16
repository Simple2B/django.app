import pytest
from users.models import CustomUser
from users.forms import UserCreateForm


@pytest.fixture
def create_user(db) -> CustomUser:
    return CustomUser.objects.create(username='test', email='test@mail.com', password='11111111')


@pytest.fixture
def create_user_form(db) -> UserCreateForm:
    return UserCreateForm(data={'username': 'test', 'email': 'test@mail.com', 'password': '11111111'})
