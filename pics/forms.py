from django import forms
from .models import UserProfile, Image
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm  
class ProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['bio','profilephoto']
class SignUpForm(UserCreationForm):
  class Meta:
    model=User
    fields=['username','first_name','last_name','email', 'password1','password2']

class CommentForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ('like',)
        widgets = {
          'comment': forms.Textarea(attrs={'rows':5, 'cols':40}),
        }

class PhotoForm(forms.ModelForm):
    class Meta:
        model=Image
        fields=['name','image','caption']