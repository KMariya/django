from rest_framework import serializers

from .models import News
from .models import Rest

class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

    def validate_text(self, value):

        keyword = "Важно"
        if keyword not in value:
            raise serializers.ValidationError(f"Текст новости должен содержать ключевое слово '{keyword}'.")
        return value


class RestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rest
        fields = ('author', 'title', 'text')

class RestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rest
        fields = '__all__'