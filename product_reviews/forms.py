from django import forms
from .models import Review

RATINGS = [(1, 'Indifferent'),
           (2, 'Bad'),
           (3, 'Good'),
           (4, 'Great'),
           (5, 'Brilliant!')]


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('title', 'content', 'rating')

    rating = forms.ChoiceField(label='What is your rating?',
                               choices=RATINGS,
                               widget=forms.RadioSelect)
