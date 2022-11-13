from django.shortcuts import render
from blog.models import Post
from django.utils import timezone

# Create your views here.
def index(request):
  return render(request, "blog/index.html")

def index(request):
    posts = Post.objects.filter(published_at__lte=timezone.now())
    return render(request, "blog/index.html", {"posts": posts})
    # to fetch all the Post objects in the system, and send them to the index.html template