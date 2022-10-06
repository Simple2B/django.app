from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render

from .forms import PostCreateForm
from .models import Post
from users.models import CustomUser
from .logger import logger


class CreatePost(CreateView):
    form_class = PostCreateForm
    template_name = "posts/create_post.html"
    success_url = reverse_lazy("posts_list")

    def form_valid(self, form):
        form.save()
        return redirect("posts_list")

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form = form.save(commit=False)
            form.user = CustomUser.objects.get(pk=self.request.user.pk)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class PostListView(ListView):
    model = Post
    template_name = "posts/posts_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(published=True)

    def get(self, request):
        if not self.request.user.is_authenticated:
            return redirect("login_user")
        return render(
            self.request,
            "posts/posts_list.html",
            context={"posts": self.get_queryset()},
        )


class PostDetailView(ListView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post_detail"

    def get_queryset(self):
        return Post.objects.filter(pk=self.request.resolver_match.kwargs["pk"]).first()


class PostDeleteView(DeleteView):
    model = Post
    template_name = "posts/post_delete.html"
    success_url = reverse_lazy("posts_list")


class PostUpdateView(UpdateView):
    model = Post
    fields = ["title", "content", "published"]
    template_name = "posts/post_update.html"
    success_url = reverse_lazy("posts_list")
