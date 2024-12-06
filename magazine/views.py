from django.shortcuts import render, get_object_or_404
from magazine.models import Post
from magazine.forms import EmailForm
from django.core.paginator import Paginator


def index(request):
    post = Post.objects.all()
    post_business = Post.objects.filter(category='business')[:3]
    post_travel = Post.objects.filter(category='travel')[:3]
    recently_posts = Post.objects.order_by('-id')[:4]
    category = Post.objects.values_list('category', flat=True).distinct()
    category_post = Post.objects.all()[:3]
    email_form = EmailForm()
    if request.method == 'POST':
        email_form = EmailForm(data=request.POST)
        if email_form.is_valid:
            email_form.save()
    context = {
        'index': post,
        'email_form': email_form,
        'recently_posts': recently_posts,
        'category_post': category_post,
        'categories': category,
        'post_business': post_business,
        'post_travel': post_travel,
    }
    return render(request, 'index.html', context)


def details(request, pk):
    detail = get_object_or_404(Post, id=pk)
    category = Post.objects.values_list('category', flat=True).distinct()
    post = Post.objects.all()[:3]
    email_form = EmailForm()
    if request.method == 'POST':
        email_form = EmailForm(data=request.POST)
        if email_form.is_valid:
            email_form.save()
    context = {
        'details': detail,
        'email_form': email_form,
        'posts': post,
        'categories': category,
    }
    return render(request, 'single.html', context)


def categories(request):
    category2 = Post.objects.values_list('category', flat=True).distinct()
    category = request.GET.get("category")
    posts = Paginator(Post.objects.filter(category=category), 1)
    get_page = request.GET.get("page")
    all_post = posts.get_page(get_page)
    if not get_page:
        get_page = 1
    context = {
        'page': get_page,
        'posts': all_post,
        'category': category,
        'categories': category2,
    }
    return render(request, 'categories.html', context)


def search_function(request):
    category2 = Post.objects.values_list('category', flat=True).distinct()
    search = request.GET.get('search')
    posts = Paginator(Post.objects.filter(title__icontains=search), 1)
    page = request.GET.get('page')
    paginator = posts.get_page(page)
    if not page:
        page = 1

    context = {
        'posts': posts,
        'search': search,
        'page': page,
        'paginator': paginator,
        'categories': category2,
    }
    return render(request, 'search.html', context)
