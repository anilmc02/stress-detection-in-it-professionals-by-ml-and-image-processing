from django import forms
from .models import SurveyResponseModel, RESPONSE_CHOICES

class SurveyResponseForm(forms.ModelForm):
    class Meta:
        model = SurveyResponseModel
        fields = ['question1', 'question2', 'question3','question4','question5','question6','question7','question8','question9','question10','question11','question12','question13','question14','question15']  # Add fields for the remaining 13 questions
        widgets = {
            'question1': forms.Select(choices=RESPONSE_CHOICES),
            'question2': forms.Select(choices=RESPONSE_CHOICES),
            'question3': forms.Select(choices=RESPONSE_CHOICES),
            'question4': forms.Select(choices=RESPONSE_CHOICES),
            'question5': forms.Select(choices=RESPONSE_CHOICES),
            'question6': forms.Select(choices=RESPONSE_CHOICES),
            'question7': forms.Select(choices=RESPONSE_CHOICES),
            'question8': forms.Select(choices=RESPONSE_CHOICES),
            'question9': forms.Select(choices=RESPONSE_CHOICES),
            'question10': forms.Select(choices=RESPONSE_CHOICES),
            'question11': forms.Select(choices=RESPONSE_CHOICES),
            'question12': forms.Select(choices=RESPONSE_CHOICES),
            'question13': forms.Select(choices=RESPONSE_CHOICES),
            'question14': forms.Select(choices=RESPONSE_CHOICES),
            'question15': forms.Select(choices=RESPONSE_CHOICES),
            # Add widgets for the remaining questions
        }
