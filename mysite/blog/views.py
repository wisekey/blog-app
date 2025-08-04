from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import EmailPostForm, CommentForm, SearchForm
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.http import require_POST
from taggit.models import Tag
from django.core.paginator import Paginator
from taggit.models import Tag
from django.db.models import Count
from django.contrib.postgres.search import SearchVector
from django.http import HttpRequest, HttpResponse
from django.db.models import QuerySet
from django.core.paginator import Page
from typing import TypedDict


class PostListContext(TypedDict):
    posts: Page[Post]
    tag: Tag | None


def post_list(request: HttpRequest, tag_slug: str | None = None) -> HttpResponse:
    post_list: QuerySet[Post] = Post.published.all()

    tag: Tag | None = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])

    paginator = Paginator(post_list, 3)
    page_number: str = request.GET.get("page", 1)

    posts: Page = paginator.get_page(page_number)

    context_data: PostListContext = {"posts": posts, "tag": tag}

    return render(request, "blog/post/list.html", context=context_data)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )

    comment_order = "created"
    if "desc" in request.GET:
        comment_order = "-created"

    comments = post.comments.filter(active=True).order_by(comment_order)

    form = CommentForm()

    post_tags_ids = post.tags.values_list("id", flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count("tags")).order_by(
        "-same_tags", "-publish"
    )

    return render(
        request,
        "blog/post/detail.html",
        {
            "post": post,
            "comments": comments,
            "form": form,
            "similar_posts": similar_posts,
        },
    )


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)

    sent = False

    if request.method == "POST":
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read {post.title}"
            message = (
                f"Read {post.title} at {post_url}\n\n"
                f"{cd['name']}'s ({cd['email']}) comments: {cd['comments']}"
            )
            send_mail(subject, message, settings.EMAIL_HOST_USER, [cd["to"]])
            sent = True
    else:
        form = EmailPostForm

    data = {
        "post": post,
        "form": form,
        "sent": sent,
    }

    return render(request, "blog/post/share.html", data)


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None

    comment_post = request.POST.copy()

    if request.user.is_authenticated:
        comment_post["name"] = request.user.username
        comment_post["email"] = request.user.email

    form = CommentForm(data=comment_post)

    print(form.is_valid())
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(
        request,
        "blog/post/comment.html",
        {"post": post, "form": form, "comment": comment},
    )


def post_search(request):
    form = SearchForm()
    query = None
    results = []

    if "query" in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            results = Post.published.annotate(
                search=SearchVector("title", "body")
            ).filter(search=query)

    return render(
        request,
        "blog/post/search.html",
        {"form": form, "query": query, "results": results},
    )
