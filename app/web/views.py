from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Post

POSTS_PER_PAGE = 12


def list_view(request):
    search = request.GET.get("search")
    page = request.GET.get("page")
    posts = Post.objects.all()
    if search:
        posts = posts.filter(title__icontains=search)

    paginator = Paginator(posts, POSTS_PER_PAGE)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        "posts": posts,
        "search": search or "",
    }
    return render(request, "list.html", context)
