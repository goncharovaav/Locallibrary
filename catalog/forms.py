from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Book
import datetime


class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
        return data

class BookForm(forms.ModelForm):
    class Meta: 
        model = Book
        fields = ['title', 'author', 'summary', 'isbn', 'genre']
        widgets = {
            'title': forms.TextInput(attrs={'maxlength': 5})
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'summary', 'isbn', 'genre']
        widgets = {
            'title': forms.TextInput(attrs={'maxlength': 5}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 5:
            raise ValidationError(_('Не менее 5'))
        return title