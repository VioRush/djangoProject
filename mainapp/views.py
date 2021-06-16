from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Post, Comment
# Create your views here.


def index(request):   # tu zamiescić co chcemy zeby zostalo wyswietlone po uruchomieniu .../blog
    # return HttpResponse("To jest blog!!!.")
    return render(request, 'mainapp/base.html')


def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'mainapp/home.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    images = post.imagies.all()
    comments = post.comments.all()
    return render(request, 'mainapp/post_detail.html', {'post': post, 'comments': comments, 'images': images})









