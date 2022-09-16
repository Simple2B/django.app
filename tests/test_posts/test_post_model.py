from tests.conftest import create_posts, RANGE_COUNT
from posts.models import Post


def test_create_posts(create_posts):
    posts = Post.objects.all()
    assert len(posts) == RANGE_COUNT
    for i in range(RANGE_COUNT):
        assert posts[i].pk == i + 1
        assert posts[i].title == f'title {i}'
