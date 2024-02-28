from django.shortcuts import render

posts = [
    {
        "author": "KLombe",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "February 28, 2018"
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "February 27^n, 2018"
    }
]


def home(request):
    context = {
        "posts": posts
    }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
