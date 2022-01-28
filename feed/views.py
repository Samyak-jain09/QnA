
from django.views.generic import DetailView, TemplateView,ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

from followers.models import Follower

from .models import Post


class MyFeed(TemplateView):
    http_method_names = ["get"]
    template_name = "feed/homepage.html"

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if self.request.user.is_authenticated:
            following = list(
                Follower.objects.filter(followed_by=self.request.user).values_list('following', flat=True)
            )
            if not following:
                # Show the default 30
                posts = None
            else:
                posts = Post.objects.filter(author__in=following).order_by('-id')[0:60]
        else:
            posts = Post.objects.all().order_by('-id')[0:30]
        context['posts'] = posts
        return context

class HomePage(ListView):
    http_method_names=["get"]
    template_name="feed/homepage.html"
    model=Post
    context_object_name="posts"
    queryset=Post.objects.all().order_by("-id")[0:30]


class PostDetailView(DetailView):
    http_method_names = ["get"]
    template_name = "feed/detail.html"
    model = Post
    context_object_name = "post"


class CreateNewPost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "feed/create.html"
    fields = ['text','image']
    success_url = "/"

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):

        post = Post.objects.create(
            text=request.POST.get("text"),
            # image=request.POST.get("image"),
            author=request.user,
        )

        return render(
            request,
            "includes/post.html",
            {
                "post": post,
                "show_detail_link": True,
            },
            content_type="application/html"
        )



