from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    """
    A view to show article form
    """
    class Meta:
        model = Article
        fields = ('title', 'excerpt',
                  'featured_image', 'content')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded'
