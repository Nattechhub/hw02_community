from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    post_per_page = 10
    template = 'posts/index.html'
    posts = Post.objects.all().order_by('-pub_date')[:post_per_page]
    context = {'posts': posts}
    return render(request, template, context)


def group_posts(request, slug):
    post_per_page = 10
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all().order_by('-pub_date')[:post_per_page]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
