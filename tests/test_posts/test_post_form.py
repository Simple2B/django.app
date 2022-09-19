from tests.conftest import create_posts_form, RANGE_COUNT
from posts.models import Post
from posts.forms import PostUpdateForm


def test_create_posts(create_posts_form):
    for i in range(RANGE_COUNT):
        create_posts_form[i].save()
        post = Post.objects.get(pk=i+1)
        assert post
        assert post.title == f'title {i}'


def test_update_post(create_posts):
    PostUpdateForm(data={'id': 1, 'title': 'title 0',
                   'content': 'changed content', 'published': False}).save()
    post = Post.objects.get(pk=1)
    assert post.content == 'changed content'
    assert not post.published
