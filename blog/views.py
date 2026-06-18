# blog/views.py

from django.shortcuts import render, get_object_or_404

from .models import Blog
from common.models import *


def blogs(request):

    blogs = Blog.objects.order_by(
        '-created_at'
    )
    categories = BlogCategory.objects.all()
    sliders = Slider.objects.filter(is_active=True, page='blog').order_by('order')

    category_id = request.GET.get('category')

    if category_id:
        blogs = blogs.filter(category_id=category_id)

    context = {
        'blogs': blogs,
        'categories': categories,
        'current_category': category_id,
        'sliders': sliders,

    }

    return render(
        request,
        'news-grid.html',
        context
    )
from django.shortcuts import render, get_object_or_404
from .models import Blog, BlogCategory

from  company.models import *
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, BlogCategory, BlogReview


def blog_detail(request, slug):

    blog = get_object_or_404(Blog, slug=slug)
    sliders = Slider.objects.filter(is_active=True, page='blog-details').order_by('order')

    # VIEWS
    blog.views += 1
    blog.save()

    # REVIEW SAVE
    if request.method == 'POST':

        BlogReview.objects.create(

            blog=blog,

            name=request.POST.get('name'),

            email=request.POST.get('email'),

            message=request.POST.get('message')

        )

        return redirect(
            'blog_detail',
            slug=blog.slug
        )

    # SIDEBAR
    popular_blogs = Blog.objects.order_by('-views')[:4]

    related_blogs = Blog.objects.filter(
        category=blog.category
    ).exclude(
        id=blog.id
    ).order_by('-created_at')[:4]

    categories = BlogCategory.objects.all()

    # REVIEWS
    reviews = blog.reviews.all().order_by('-created_at')

    context = {

        'blog': blog,
        'sliders': sliders,

        'popular_blogs': popular_blogs,

        'related_blogs': related_blogs,

        'categories': categories,

        'reviews': reviews,
    }

    return render(
        request,
        'news-details.html',
        context
    )
def blog_details(request, slug):

    blog = get_object_or_404(
        Blog,
        slug=slug
    )

    blog.views += 1
    blog.save()

    related_blogs = Blog.objects.exclude(
        id=blog.id
    )[:3]

    return render(
        request,
        'news-details.html',
        {
            'blog': blog,
            'related_blogs': related_blogs
        }
    )


# views.py

from django.shortcuts import render, get_object_or_404
from .models import Blog, BlogCategory


def blogss(request):

    blogs = Blog.objects.select_related('category').order_by('-created_at')

    categories = BlogCategory.objects.all()

    category_id = request.GET.get('category')

    if category_id:
        blogs = blogs.filter(category_id=category_id)

    context = {
        'blogs': blogs,
        'categories': categories,
        'current_category': category_id,
    }

    return render(request, 'blog/blogs.html', context)


def blog_details(request, slug):

    blog = get_object_or_404(Blog, slug=slug)

    blog.views += 1
    blog.save()

    related_blogs = Blog.objects.filter(
        category=blog.category
    ).exclude(id=blog.id).order_by('-created_at')[:3]

    context = {
        'blog': blog,
        'related_blogs': related_blogs,
    }

    return render(request, 'blog/blog_detail.html', context)

