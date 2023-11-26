from django.core.management.base import BaseCommand
from myapp.models import Comment, News  # Замените "myapp" на имя вашего приложения

class Command(BaseCommand):
    help = 'Вычисляет общее количество комментариев для каждой новости'

    def handle(self, *args, **options):
        news_ids = News.objects.values_list('id', flat=True)

        for news_id in news_ids:
            comment_count = Comment.objects.filter(post_id=news_id).count()
            self.stdout.write(self.style.SUCCESS(f"Общее количество комментариев для новости с ID {news_id}: {comment_count}"))