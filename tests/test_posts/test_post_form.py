from tests.conftest import create_posts_form, RANGE_COUNT
from posts.models import Post


def test_create_posts(create_posts_form):
    for i in range(RANGE_COUNT):
        assert create_posts_form[i].is_valid()
