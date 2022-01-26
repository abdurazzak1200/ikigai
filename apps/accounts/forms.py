from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'inst']
        widgets = {
            'image': forms.FileInput(attrs={'style':'width:100%'}),
            'bio': forms.Textarea(attrs={'style':'width:100%'}),
            'inst': forms.URLInput(attrs={'style':'width:100%'})
        }