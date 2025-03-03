from django import forms
from .models import Post, Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating','comment']
        widgets = {
            'rating': forms.Select(attrs={'class':'form-control'},choices=((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'))),
            'comment': forms.Textarea(attrs={'class':'form-control'}),
        }