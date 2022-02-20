from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post
from .forms import PostForm
from .filters import PostFilter

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

def index(request):
    posts = Post.objects.filter(active=True, featured=True).order_by('num')[0:3]
    
    context = {
        "posts" : posts
    }
    return render(request, 'home/index.html', context)


def posts(request):
    posts = Post.objects.all()
    myFilter = PostFilter(request.GET, queryset=posts)
    posts = myFilter.qs

    page = request.GET.get('page')
    paginator = Paginator(posts, 6)
    try :
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage :
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts' : posts,
        'myfilter' : myFilter,

    }
    return render(request, 'home/posts.html', context)
    
def post(request, slug):
    posts = Post.objects.get(slug=slug)

    context = {
        'post' : posts
    }
    return render(request, 'home/post.html', context )
    


# Create Posts

@login_required(login_url="home:index")
def create_post(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home:posts')
    context = {
        'form' : form
    }
    return render(request, "backend/post_form.html", context)

    
@login_required(login_url="home:index")
def update_post(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home:posts')
    context = {
        'form' : form
    }
    return render(request, "backend/post_form.html", context)

@login_required(login_url="home:index")
def delete_post(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == "POST":
        post.delete()
        return redirect('home:posts')
    context = {
        "item":post
    }
    return render(request, "backend/delete_post.html", context)


#Contant
def sendEmail(request):
    if request.method == 'POST' :
        template = render_to_string('contact/email_template.html',{
            'name' : request.POST['name'],
            'phone' : request.POST['phone'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        })

        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['omar90180360@gmail.com']
        )
        email.fail_silently = False
        email.send()

    return render(request, "contact/email_sent.html")