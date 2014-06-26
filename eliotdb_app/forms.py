from django import forms

class SearchForm(forms.Form):
    "Search the names table by name."
    name = forms.CharField(required=False)
    
    def clean(self):
        """Custom form validation."""
        cleaned_data = self.cleaned_data

        name = cleaned_data.get('name')
      
        "Validate at least one term has been entered"
        if not name :
            del cleaned_data['name']
            raise forms.ValidationError("Please enter search terms.")

        return cleaned_data
