from tests.conftest import create_user, create_user_form
from users.models import CustomUser


def test_user_form(create_user_form):
    assert create_user_form.is_valid()


def test_user_form_create(create_user_form):
    create_user_form.save()
    user = CustomUser.objects.get(pk=1)
    assert user.username == 'test'
    assert user.email == 'test@mail.com'
