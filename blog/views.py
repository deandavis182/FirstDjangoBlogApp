from blog.forms import *
from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import *

from blog.models import Post


# Create your views here.

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email'],
            #date=datetime.date()
            )
            user.save()
            return HttpResponseRedirect('/register/success/')

    else:
        form = RegistrationForm()
    variables = {
    'form': form
    }

    return render_to_response(
        'registration/register.html',
        variables,
    )


def register_success(request):
    return render_to_response(
    'registration/success.html',
    )


def index(request):
    if request.method == 'POST':
        newpost = request.POST
        if newpost:
            post = Post(
            title=newpost['Title'],
            slug=newpost['Title'],
            description=newpost['Description'],
            content=newpost['post_content'],
            published=newpost['Publish'],
            users_id=request.user,
            )
            post.save()
            return HttpResponseRedirect('/')

    # get the blog posts that are published
    posts = Post.objects.filter(published=True)
    # now return the rendered template
    return render(request, 'blog/index.html', {'posts': posts, 'user': request.user})


def user_home(request):
    if not request.user.id:
        return HttpResponseRedirect('/login/')
    # get the posts specific to current user
    allposts = Post.objects.filter(users_id_id=request.user.id)
    pubposts = []
    unpubposts = []
    for post in allposts:
        if post.published == True:
            pubposts.append(post)
        else:
            unpubposts.append(post)
    shpubposts = pubposts[:4]
    shmpubposts = pubposts[4:]
    shunpubposts = unpubposts[:4]
    shmunpubposts = unpubposts[4:]
    return render(request, 'blog/user_home.html', {'allposts': allposts, 'shpubposts': shpubposts, 'shmpubposts': shmpubposts, 'shunpubposts': shunpubposts, 'shmunpubposts': shmunpubposts, 'user': request.user})


def post(request, id):
    # get the Post object
    post = Post.objects.get(id=id)
    # now return the rendered template
    return render(request, 'blog/post.html', {'post': post})






