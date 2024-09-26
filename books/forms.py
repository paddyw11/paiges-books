from django import forms
from .models import Book, Genre

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        genre = Genre.objects.all()
        friendly_names = [(g.id, g.get_friendly_name()) for g in genres]

        self.fields['genre'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'