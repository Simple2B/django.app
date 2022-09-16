import pytest
from users.models import CustomUser
from users.forms import UserCreateForm
from posts.models import Post
from posts.forms import PostCreateForm


RANGE_COUNT = 3


@pytest.fixture
def create_user(db) -> CustomUser:
    return CustomUser.objects.create(username='test', email='test@mail.com', password='11111111bbb')


@pytest.fixture
def create_user_form(db) -> UserCreateForm:
    return UserCreateForm(data={'username': 'test', 'email': 'test@mail.com', 'password1': '11111111bbb', 'password2': '11111111bbb'})


@pytest.fixture
def create_posts(create_user) -> None:
    [Post.objects.create(title=f'title {i}', content=f'test content {i}',
                         published=True, user=create_user) for i in range(RANGE_COUNT)]


@pytest.fixture
def create_posts_form(create_user) -> list:
    return [PostCreateForm(data={'title': f'title {i}', 'content': f'test content {i}', 'published': True, 'user': create_user}) for i in range(RANGE_COUNT)]
