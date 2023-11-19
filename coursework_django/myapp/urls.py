from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import contact_view

urlpatterns = [

    path('', views.index, name='index'),
    path('news', views.news, name='news'),
    path('rest', views.rest, name='rest'),
    path('profile', views.profile, name='profile'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('comment_submit', views.comment_submit, name='comment_submit'),
    path('form', contact_view, name='form'),
    path('news/', views.NewsListView.as_view())

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
