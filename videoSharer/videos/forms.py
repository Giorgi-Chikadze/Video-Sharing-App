from django import forms

class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'placeholder': 'leave a comment'
        }
    ))
