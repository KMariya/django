from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from simple_history.models import HistoricalRecords

class News(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(null=True, blank=True, default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    history = HistoricalRecords()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



class Rest(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    history = HistoricalRecords()

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Rest', on_delete=models.CASCADE, default=1)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment #{self.id}"

phone_regex = RegexValidator(
    regex=r'^\+7\d{10}$',
    message="Номер телефона должен быть в формате: '+79999999999"
)

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(validators=[phone_regex], max_length=15)
    message = models.TextField()


    def __str__(self):
        return self.name