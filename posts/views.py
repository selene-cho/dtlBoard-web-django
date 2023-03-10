from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import redirect
from .models import Post


def index(request):
    return render(request, "posts/index.html")


def post_list(request):
    posts = Post.objects.all()
    return render(request, "posts/list.html", {"posts": posts})


class PostUploadView(CreateView):
    model = Post
    fields = ["title", "photo", "text"]
    template_name = "posts/upload.html"

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect("/list")
        else:
            return self.render_to_response({"form": form})


class PostDeleteView(DeleteView):
    model = Post
    success_url = "/list"
    template_name = "posts/delete.html"


class PostUpdateView(UpdateView):
    model = Post
    fields = ["title", "photo", "text"]
    template_name = "posts/update.html"
