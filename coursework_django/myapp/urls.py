from django.urls import path, include
from rest_framework import routers

from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import contact_view, NewsListView
from .views import create_news
from .views import RestListAllView

router = routers.DefaultRouter()
router.register(r'rest', RestListAllView, basename='rest')


urlpatterns = [

    path('', views.index, name='index'),
    path('news', views.news, name='news'),
    path('rest', views.rest, name='rest'),
    path('profile', views.profile, name='profile'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('comment_submit', views.comment_submit, name='comment_submit'),
    path('form', contact_view, name='form'),
    path('news/api', views.NewsListView.as_view()),
    path('rest/api', views.RestListView.as_view()),
    path('create', create_news, name='create_news'),
    path('api/', include(router.urls))





] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
