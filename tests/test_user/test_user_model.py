from users.models import CustomUser
from tests.conftest import create_user


def test_user(create_user):
    user = CustomUser.objects.get(pk=1)
    assert user.username == 'test'
    assert user.email == 'test@mail.com'
