from django import forms

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=255, required=True)
    author = forms.CharField(max_length=255, required=True)
    published_date = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    def clean_title(self):
        title = self.cleaned_data.get('title', '').strip()
        if not title:
            raise forms.ValidationError("Title cannot be empty.")
        return title

    def clean_author(self):
        author = self.cleaned_data.get('author', '').strip()
        if not author:
            raise forms.ValidationError("Author cannot be empty.")
        return author
