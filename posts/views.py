from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .forms import PostCreateForm
from .models import Post


class CreatePost(CreateView):
    form_class = PostCreateForm
    template_name = 'posts/create_post.html'
    success_url = reverse_lazy('posts_list')

    def form_valid(self, form):
        form.save()
        return redirect('posts_list')


class PostListView(ListView):
    model = Post
    template_name = 'posts/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(published=True)
