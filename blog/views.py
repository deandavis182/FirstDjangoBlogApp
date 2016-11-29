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
    	    # assign form from 'forms.py' containing posts data
        form = RegistrationForm(request.POST)
        if form.is_valid():
        	# create a built-in django User object with data from form
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email'],
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
	# if user fills out 'new post' form
    if request.method == 'POST':
    	# grab post data
        newpost = request.POST
        if newpost:
        	# assign values to Post object from models
            post = Post(
            title=newpost['Title'],
            slug=newpost['Title'],
            description=newpost['Description'],
            content=newpost['post_content'],
            published=newpost['Publish'],
            users_id=request.user,
            )
            # save new Post object
            post.save()
            return HttpResponseRedirect('/')

    # get the blog posts that are published
    posts = Post.objects.filter(published=True)
    # now return the rendered template
    return render(request, 'blog/index.html', {'posts': posts, 'user': request.user})


def user_home(request):
	# make sure there is a logged in user to access this view
    if not request.user.id:
        return HttpResponseRedirect('/login/')
    # get the posts specific to current user
    allposts = Post.objects.filter(users_id_id=request.user.id)
    # make empty list of published posts
    pubposts = []
    # make empty list of unpublished posts
    unpubposts = []
    # now append the published and unpublished posts
    for post in allposts:
        if post.published == True:
            pubposts.append(post)
        else:
            unpubposts.append(post)
        # assign first 4 published posts to display
    shpubposts = pubposts[:4]
        # assign the remaining published posts
    shmpubposts = pubposts[4:]
    # assign first 4 UNpublished posts to display
    shunpubposts = unpubposts[:4]
    # assign the remaining UNpublished posts
    shmunpubposts = unpubposts[4:]
    # now render the template with the assigned post variables
    return render(request, 'blog/user_home.html', {'allposts': allposts, 'shpubposts': shpubposts, 'shmpubposts': shmpubposts, 'shunpubposts': shunpubposts, 'shmunpubposts': shmunpubposts, 'user': request.user})


def post(request, id):
    # get the Post object
    post = Post.objects.get(id=id)
    # now return the rendered template
    return render(request, 'blog/post.html', {'post': post})






