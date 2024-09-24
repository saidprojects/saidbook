from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.models import Post, Comment
from blog.forms import CommentForm, SearchForm
from django.db.models import Q

# index.html
def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts" : posts,
    }
    return render(request, r"blog/index.html", context=context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains = category
    ).order_by("-created_on")
    context = {}
    if len(posts) == 0 :
        context = {
        "category" : category,
        "pusto": "( Пока пусто )",
        "posts" : posts,
        }
    else:
        context = {
        "category" : category,
        "pusto": " ",
        "posts" : posts,
        }
    return render(request, r"blog/category.html", context=context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm(),
    }
    return render(request, "blog/detail.html", context)

def blog_search(request):
    form = SearchForm()
    results = []
    status = " "
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.objects.filter( Q(title__icontains=query) &
                                           ~Q(categories__name__contains= "Твиты")
                                           ).order_by("-created_on")
        
            if results:
                status = "ok"
            else:
                status = "Нет результатов"

    
    context = {
        "form": SearchForm(),
        "results": results,
        "status": status,
    }
    return render(request, 'blog/search.html', context=context)
