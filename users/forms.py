from django import forms
from .models import UserRegistrationModel


class UserRegistrationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'pattern': '[a-zA-Z]+'}), required=True, max_length=100)
    loginid = forms.CharField(widget=forms.TextInput(attrs={'pattern': '[a-zA-Z]+'}), required=True, max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'pattern': '(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}',
                                                                 'title': 'Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters'}),
                               required=True, max_length=100)
    mobile = forms.CharField(widget=forms.TextInput(attrs={'pattern': '[56789][0-9]{9}'}), required=True,
                             max_length=100)
    email = forms.CharField(widget=forms.TextInput(attrs={'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'}),
                            required=True, max_length=100)
    locality = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 22}), required=True, max_length=250)
    city = forms.CharField(widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'pattern': '[A-Za-z ]+', 'title': 'Enter Characters Only '}), required=True,
                           max_length=100)
    state = forms.CharField(widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'pattern': '[A-Za-z ]+', 'title': 'Enter Characters Only '}), required=True,
                            max_length=100)
    status = forms.CharField(widget=forms.HiddenInput(), initial='waiting', max_length=100)

    class Meta():
        model = UserRegistrationModel
        fields = '__all__'

from django import forms
from .models import SurveyResponseModel, RESPONSE_CHOICES
from .survey_response_form import SurveyResponseForm

# class SurveyResponseForm(forms.ModelForm):
#     class Meta:
#         model = SurveyResponseModel
#         fields = ['question1', 'question2', 'question3','question4','question5','question6','question7','question8','question9','question10','question11','question12','question13','question14','question15']  # Add fields for the remaining 13 questions
#         widgets = {
#             'question1': forms.Select(choices=RESPONSE_CHOICES),
#             'question2': forms.Select(choices=RESPONSE_CHOICES),
#             'question3': forms.Select(choices=RESPONSE_CHOICES),
#             'question4': forms.Select(choices=RESPONSE_CHOICES),
#             'question5': forms.Select(choices=RESPONSE_CHOICES),
#             'question6': forms.Select(choices=RESPONSE_CHOICES),
#             'question7': forms.Select(choices=RESPONSE_CHOICES),
#             'question8': forms.Select(choices=RESPONSE_CHOICES),
#             'question9': forms.Select(choices=RESPONSE_CHOICES),
#             'question10': forms.Select(choices=RESPONSE_CHOICES),
#             'question11': forms.Select(choices=RESPONSE_CHOICES),
#             'question12': forms.Select(choices=RESPONSE_CHOICES),
#             'question13': forms.Select(choices=RESPONSE_CHOICES),
#             'question14': forms.Select(choices=RESPONSE_CHOICES),
#             'question15': forms.Select(choices=RESPONSE_CHOICES),
#             # Add widgets for the remaining questions
#         }

class SurveyResponseForm(forms.ModelForm):
    # Define each question as a separate field with choices
    question1 = forms.ChoiceField(
        label="1) Are you experiencing difficulty falling asleep or staying asleep due to work-related concerns?",
        choices=[
            ('a', 'Yes, frequently'),
            ('b', 'Occasionally'),
            ('c', 'Rarely'),
            ('d', 'Not at all')
        ],
        widget=forms.RadioSelect
    )
    question2 = forms.ChoiceField(
        label="2) Do you often find yourself feeling overwhelmed by the workload?",
        choices=[
            ('a', 'Yes, frequently'),
            ('b', 'Sometimes'),
            ('c', 'Rarely'),
            ('d', 'Not at all')
        ],
        widget=forms.RadioSelect
    )
    question3 = forms.ChoiceField(
        label="3) Are you frequently irritable or short-tempered with colleagues or family members?",
        choices=[
            ('a', 'Yes, frequently'),
            ('b', 'Occasionally'),
            ('c', 'Rarely'),
            ('d', 'Not at all')
        ],
        widget=forms.RadioSelect
    )
    question4 = forms.ChoiceField(
        label="4) Have you noticed changes in your eating habits, such as overeating or loss of appetite?",
        choices=[
            ('a', 'Yes, frequently'),
            ('b', 'Sometimes'),
            ('c', 'Rarely'),
            ('d', 'Not at all')
        ],
        widget=forms.RadioSelect
    )
    question5 = forms.ChoiceField(
        label="5) Are you relying on caffeine or other stimulants to keep you alert during the day?",
        choices=[
            ('a', 'Yes, frequently'),
            ('b', 'Occasionally'),
            ('c', 'Rarely'),
            ('d', 'Not at all')
        ],
        widget=forms.RadioSelect
    )
    question6 = forms.ChoiceField(
        label="6) Have you lost interest in activities or hobbies you once enjoyed?",
        choices=[
            ('a', 'Yes, frequently'),
            ('b', 'Sometimes'),
            ('c', 'Rarely'),
            ('d', 'Not at all')
        ],
        widget=forms.RadioSelect
    )
    question7 = forms.ChoiceField(
        label="7) Are you experiencing physical symptoms like headaches, muscle tension, or digestive issues?",
        choices=[
            ('a', 'Yes, frequently'),
            ('b', 'Occasionally'),
            ('c', 'Rarely'),
            ('d', 'Not at all')
        ],
        widget=forms.RadioSelect
    )
    question8 = forms.ChoiceField(
        label="8) Have you neglected self-care, such as exercise or regular medical check-ups?",
        choices=[
            ('a', 'Yes, frequently'),
            ('b', 'Occasionally'),
            ('c', 'Rarely'),
            ('d', 'Not at all')
        ],
        widget=forms.RadioSelect
    )
    question9 = forms.ChoiceField(
        label="9) Are you frequently working long hours, including weekends and holidays?",
        choices=[
            ('a', 'Yes, frequently'),
            ('b', 'Sometimes'),
            ('c', 'Rarely'),
            ('d', 'Not at all')
        ],
        widget=forms.RadioSelect
    )
    question10 = forms.ChoiceField(
        label="10) Do you feel that your contributions at work are not appreciated or recognized?",
        choices=[
            ('a', 'Yes, frequently'),
            ('b', 'Sometimes'),
            ('c', 'Rarely'),
            ('d', 'Not at all')
        ],
        widget=forms.RadioSelect
    )
    question11 = forms.ChoiceField(
        label="11) Do you have difficulty setting clear boundaries with your supervisors or colleagues?",
        choices=[
            ('a', 'Yes, frequently'),
            ('b', 'Sometimes'),
            ('c', 'Rarely'),
            ('d', 'Not at all')
        ],
        widget=forms.RadioSelect
    )
    question12 = forms.ChoiceField(
        label="12) Do you frequently experience technology-related frustrations or setbacks?",
        choices=[
            ('a', 'Yes, frequently'),
            ('b', 'Sometimes'),
            ('c', 'Rarely'),
            ('d', 'Not at all')
        ],
        widget=forms.RadioSelect
    )
    question13 = forms.ChoiceField(
        label="13) Have you had conflicts with coworkers or supervisors that cause you stress?",
        choices=[
            ('a', 'Yes, frequently'),
            ('b', 'Sometimes'),
            ('c', 'Rarely'),
            ('d', 'Not at all')
        ],
        widget=forms.RadioSelect
    )
    question14 = forms.ChoiceField(
        label="14) Are you neglecting breaks or time for relaxation during the workday?",
        choices=[
            ('a', 'Yes, frequently'),
            ('b', 'Occasionally'),
            ('c', 'Rarely'),
            ('d', 'Not at all')
        ],
        widget=forms.RadioSelect
    )
    question15 = forms.ChoiceField(
        label="15) Have you seen a significant increase in your workload without additional support or resources?",
        choices=[
            ('a', 'Yes, frequently'),
            ('b', 'Sometimes'),
            ('c', 'Rarely'),
            ('d', 'Not at all')
        ],
        widget=forms.RadioSelect
    )

    class Meta:
        model = SurveyResponseModel
        fields = [
            'question1', 'question2', 'question3', 'question4', 'question5',
            'question6', 'question7', 'question8', 'question9', 'question10',
            'question11', 'question12', 'question13', 'question14', 'question15'
        ]