from tests.conftest import create_posts
from posts.models import Post


def test_create_posts(create_posts):
    posts = Post.objects.all()
    assert len(posts) == 3
    for i in range(3):
        assert posts[i].pk == i + 1
        assert posts[i].title == f'title {i}'
