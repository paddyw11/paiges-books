from django import forms
from .widgets import CustomClearableFileInput
from .models import Book, Genre
"""
forms.py for books app
"""


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'

    image = forms.ImageField(label='image',
                             required=False, widget=CustomClearableFileInput)
    blurb = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 5,
        'class': 'border-black rounded-10',
        'placeholder': 'Enter the blurb here...',
        }), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        genre = Genre.objects.all()

        self.fields['genres'].queryset = Genre.objects.all()
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-10'
