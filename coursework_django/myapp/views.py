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

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics
from .serializers import NewsListSerializer
from .serializers import RestListSerializer

from django.db.models import Q
import django_filters
class NewsFilter(django_filters.FilterSet):
    queryset = News.objects.all()
    class Meta:
        model = News
        fields = ['author', 'title', 'text', 'created_date', 'published_date']
class NewsListView(generics.ListAPIView):
    serializer_class = NewsListSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = NewsFilter

    def get_queryset(self):
        """
        возвращает список всех новостей,
        относящихся к текущему аутентифицированному пользователю.
        """
        user = self.request.user

        # Проверка, аутентифицирован ли пользователь
        if user.is_authenticated:
            return News.objects.filter(author=user).order_by('-created_date')
        else:
            # Если пользователь не аутентифицирован, возвращайте пустой набор
            return News.objects.none()


class RestListView(generics.ListAPIView):
    queryset = Rest.objects.all()
    serializer_class = RestListSerializer

class RestListAllView(viewsets.ModelViewSet):
    queryset = Rest.objects.all()
    serializer_class = RestListSerializer

    @action(detail=False, methods=['GET'])
    def all(self, request):
        queryset = self.queryset
        serialized_data = self.get_serializer(queryset, many=True).data
        return Response(serialized_data)

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
    newss = News.objects.all().order_by('-created_date')
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


def rest(request):
    rests = Rest.objects.filter(
        Q(text__icontains='Итальянская') | Q(text__icontains='веганов') & ~Q(text__icontains='Русская')
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