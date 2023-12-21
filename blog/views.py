
from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def post_list(request):

    post_lists = Post.published.all()

    paginator = Paginator(post_lists, 2)
    page_number = request.GET.get('page', 1) 

    try:
        posts = paginator.page(page_number)

    except PageNotAnInteger:
        posts = paginator.page(1)
        
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

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
    