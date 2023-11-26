from import_export import resources

from .models import News
from .models import Rest

class NewsResource(resources.ModelResource):
    class Meta:
        model = News
        fields = ('author', 'image', 'title', 'text', 'created_date', 'published_date')

class RestResource(resources.ModelResource):
    class Meta:
        model = Rest
        fields = ('author', 'image', 'title', 'text', 'created_date', 'published_date')