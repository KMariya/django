from django import forms
from .models import ContactMessage
from .models import News
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ('name', 'phone', 'message')


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['author', 'title', 'text', 'created_date']

    def clean_text(self):

        data = self.cleaned_data['text']
        if "Важно" not in data:
            raise forms.ValidationError("Текст новости должен содержать ключевое слово 'Важно'.")
        return data