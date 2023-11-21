from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from .models import News
from .models import Rest
from .models import Comment
from .forms import ContactForm
from .forms import NewsForm

from rest_framework import generics
from .serializers import NewsListSerializer
from .serializers import RestListSerializer

from django.db.models import Q


class NewsListView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer

class RestListView(generics.ListAPIView):
    queryset = Rest.objects.all()
    serializer_class = RestListSerializer

def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'users/login.html')

def recipes(request):
    return render(request, 'recipes.html')


def profile(request):
    return render(request, 'profile.html')


def signup(request):
    return render(request, 'users/signup.html')


def news(request):

    newss = News.objects.filter(
        Q(title__startswith='В') & (Q(text__contains='ужин') | Q(text__contains='рестораны')) & ~Q(text__contains='место'),
        published_date__lte=timezone.now()
    ).order_by('-published_date')
    return render(request, 'News.html', {'newss': newss})

def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
    else:
        form = NewsForm()

    return render(request, 'create_news.html', {'form': form})

# def news(request):
#     newss = News.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
#     return render(request, 'News.html', {'newss': newss})


# def rest(request):
#     rests = Rest.objects.all().prefetch_related('comment_set')
#     return render(request, 'Rest.html', {'rests': rests})

def rest(request):
    rests = Rest.objects.filter(
        Q(text__icontains='Русская') | Q(text__icontains='Морепродукты') & ~Q(text__icontains='Японская')
    ).prefetch_related('comment_set')

    return render(request, 'Rest.html', {'rests': rests})


def comment_submit(request):
    if request.method == 'POST':
        comment_content = request.POST.get('comment_content')
        post_id = request.POST.get('post_id')

        post = Rest.objects.get(pk=post_id)
        comment = Comment(post=post, author=request.user, content=comment_content, created_at=timezone.now())
        comment.save()

        return HttpResponseRedirect('/rest')

    return render(request, 'rest.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thanks.html')
    else:
        form = ContactForm()
    return render(request, 'form.html', {'form': form})