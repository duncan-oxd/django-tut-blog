from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def single_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/single_post.html', {'post': post})
