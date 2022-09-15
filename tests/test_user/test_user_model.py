from tests.conftest import create_user
from users.models import CustomUser


def create_user(create_user):
    user = CustomUser.objects.get(pk=1)
    assert user.name == 'test'
    assert user.email == 'test@mail.com'
