from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import BlogPostForm


# Create your views here.
def blog(request):
    """
    To view all published blog posts
    """
    all_posts = Post.objects.filter(status=1).order_by("-created_on")

    context = {
        'posts': all_posts
    }

    return render(request, 'blogs.html', context)


def post_detail(request, post):
    """ To view individual blog post """

    post = get_object_or_404(Post, slug=post)

    context = {
        'post': post
    }

    return render(request, 'post_detail.html', context)


@login_required()
def add_post(request):
    """ Add a blog post via an admin panel """
    if not request.user.is_superuser:
        messages.error(request, 'Site administrator access only.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog post added successfully')
            return redirect(reverse('blog'))
        else:
            messages.error(
                request, 'Failed to add blog post, Please check the \
                    form is valid.')
    else:
        form = BlogPostForm()

    context = {
        'form': form,
    }

    return render(request, 'blog/add_post.html', context)


@login_required
def edit_post(request, post):
    """ Edit a post """
    if not request.user.is_superuser:
        messages.error(request, 'Site administrator access only.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, slug=post)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated this product!')
            return redirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(
                request, 'Failed to update this product. \
                    Please check the form is valid.')
    else:
        form = BlogPostForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template = 'edit_post.html'
    context = {
        'form': form,
        'post': post
    }

    return render(request, template, context)


@login_required
def delete_post(request, post):
    """ Delete a post """
    if not request.user.is_superuser:
        messages.error(request, 'Site administrator access only.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, slug=post)
    post.delete()
    messages.success(request, 'Post has successfully deleted!')

    return redirect(reverse('blog'))
