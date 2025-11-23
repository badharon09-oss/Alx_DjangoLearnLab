from django import forms

class BookSearchForm(forms.Form):
    search = forms.CharField(required=False)
class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "publication_year"]
