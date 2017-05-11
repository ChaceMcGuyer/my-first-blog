from django import forms
from .models import Tutorials

class TutorialsForm(forms.ModelForm):

    class Meta:
        model = Tutorials
        fields = ('language','title', 'text_one', 'code_one', 'text_two', 'code_two', 'image')
