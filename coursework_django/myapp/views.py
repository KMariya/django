from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from .models import News
from .models import Rest
from .models import Comment
from .forms import ContactForm

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import NewsListSerializer

class NewsListView(APIView):
    def get(self, request):
        news = News.objects.all()
        serializer = NewsListSerializer(news, many=True)
        return Response(serializer.data)


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def news(request):
    return render(request, 'news.html')


def rest(request):
    return render(request, 'rest.html')


def recipes(request):
    return render(request, 'recipes.html')


def profile(request):
    return render(request, 'profile.html')


def signup(request):
    return render(request, 'signup.html')


def news(request):
    newss = News.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'News.html', {'newss': newss})


def rest(request):
    rests = Rest.objects.all().prefetch_related('comment_set')
    return render(request, 'Rest.html', {'rests': rests})


def comment_submit(request):
    if request.method == 'POST':
        comment_content = request.POST.get('comment_content')
        post_id = request.POST.get('post_id')

        post = Rest.objects.get(pk=post_id)
        comment = Comment(post=post, author=request.user, content=comment_content, created_at=timezone.now())
        comment.save()

        return HttpResponseRedirect('../rest')

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