from django.shortcuts import render, redirect
from .models import Post

# Create your views here.

# def index(request):
#     return render(request, 'index.html')


def index(request):
    if request.method == "POST":
        author = request.POST.get("author")
        text = request.POST.get("text")
        if author and text:
            Post.objects.create(author=author, text=text)
            return redirect("index")

    posts = Post.objects.all().order_by("-created_at")
    return render(request, "index.html", {"posts": posts})
