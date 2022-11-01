from django.http import Http404
from django.shortcuts import render, redirect
from .models import Blog
from apps.comment.models import Comment


def blog_view(request):
    posts = Blog.objects.all().order_by('-id')

    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    author = request.GET.get('author')
    date = request.GET.get('date')

    if cat:
        posts = posts.filter(category__title__exact=cat)

    if tag:
        posts = posts.filter(tags__title__exact=tag)

    if author:
        posts = posts.filter(author__username__exact=author)

    if date:
        posts = posts.filter(created_at__contains=date)

    context = {
        'posts': posts,
    }

    return render(request, 'blog.html', context)


def blog_single(request, pk=None):
    if request.method == "POST":
        if request.user.is_authenticated:
            message = request.POST.get('message')
            comment_id = request.POST.get('comment_id')
            top_level_comment_id = request.POST.get('top_level_comment_id')

            if message:
                comment = Comment(
                    author_id=request.user.profile.id,
                    post_id=pk,
                    message=message
                )
                if comment_id:
                    comment.parent_id = comment_id
                if top_level_comment_id:
                    comment.top_level_comment_id = top_level_comment_id
                comment.save()
                return redirect(f'/blog/{pk}#comment-list')
        return redirect('/login/')

    if pk is not None:
        post = Blog.objects.get(id=pk)
        comments = Comment.objects.filter(is_reply=False, post_id=pk)
        context = {
            'post': post,
            'comments': comments,
        }
        return render(request, 'blog-single.html', context)
    raise Http404
