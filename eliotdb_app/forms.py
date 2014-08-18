from django import forms
from eliotdb_app.models import Name, Document, Mention

class SearchName(forms.Form):
    "Search the names table by name."
    name = forms.CharField(required=False)
    
    def clean(self):
        """Custom form validation."""
        cleaned_data = self.cleaned_data

        name = cleaned_data.get('name')
              
        "Validate at least one term has been entered"
        if not name:
            del cleaned_data['name']
            raise forms.ValidationError("Please enter search terms.")

        return cleaned_data

class SearchDoc(forms.Form):
    "Search the documents table by document."
    document = forms.CharField(required=False)
    
    def clean(self):
        """Custom form validation."""
        cleaned_data = self.cleaned_data

        document = cleaned_data.get('document')
              
        "Validate at least one term has been entered"
        if not document:
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


        
