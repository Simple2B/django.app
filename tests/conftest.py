import pytest
from users.models import CustomUser


@pytest.fixture
def create_user(db) -> CustomUser:
    return CustomUser.objects.create(username='test', email='test@mail.com', password='11111111')
