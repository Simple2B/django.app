from tests.conftest import create_posts_form, RANGE_COUNT
from posts.model import Post


def test_create_posts(create_posts_form):
    for i in range(RANGE_COUNT):
        create_posts_form[i].save()
        post = Post.objects.get(pk=i+1)
        assert post
        assert post.title == f'title {i}'
