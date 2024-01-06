from django.core.management.base import BaseCommand

from myapp.models import Rest, Comment


class Command(BaseCommand):
    help = 'Вычисляет общее количество комментариев для каждого ресторана'

    def handle(self, *args, **options):
        rest_ids = Rest.objects.values_list('id', flat=True)

        for news_id in rest_ids:
            comment_count = Comment.objects.filter(post_id=news_id).count()
            self.stdout.write(self.style.SUCCESS(f"Общее количество комментариев для ресторана с ID {news_id}: {comment_count}"))