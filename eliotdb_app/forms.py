from django import forms
from eliotdb_app.models import Name, Document, Mention

class SearchForm(forms.Form):
    "Search the names table by name."
    name = forms.CharField(required=False)
    document = forms.CharField(required=False)
    
    def clean(self):
        """Custom form validation."""
        cleaned_data = self.cleaned_data

        name = cleaned_data.get('name')
        document = cleaned_data.get('document')
              
        "Validate at least one term has been entered"
        if not name and not document:
            del cleaned_data['name']
            del cleaned_data['document']
            raise forms.ValidationError("Please enter search terms.")

        return cleaned_data

class NameForm(forms.ModelForm):
    class Meta:
        model = Name

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document

class MentionForm(forms.ModelForm):
    class Meta:
        model = Mention
        exclude = ('name', 'document')


        
