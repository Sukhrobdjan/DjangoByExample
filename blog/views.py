from django.shortcuts import render, get_object_or_404
from blog.models import Post
# from django.http import Http404
from django.core.paginator import Paginator



def post_list(request):

    posts = Post.published.all()

    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)

    posts = paginator.page(page_number)

    context = {
        'posts': posts
    }

    return render(request, 'list.html', context)



def post_detail(request, year, month, day, post):

    # try:
    #     post = Post.published.get(id=id)
    # except  Post.DoesNotExist:

    #     raise Http404("No Post found.")
    
    
    post = get_object_or_404(Post, status = Post.Status.PUBLISHED,
                            slug = post,
                            publish__year = year,
                            publish__month = month,
                            publish__day = day)
    context = {
          'post': post
      }
    
    return render(request, 'detail.html', context)
    