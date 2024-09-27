from django.db import models

# Add choices for the responses
RESPONSE_CHOICES = [
    ('a', 'Yes, frequently'),
    ('b', 'Sometimes'),
    ('c', 'Rarely'),
    ('d', 'Not at all'),
]


# Create your models here.
class UserRegistrationModel(models.Model):
    name = models.CharField(max_length=100)
    loginid = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.CharField(unique=True, max_length=100)
    email = models.CharField(unique=True, max_length=100)
    locality = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.loginid

    class Meta:
        db_table = 'UserRegistrations'
class UserImagePredictinModel(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    loginid = models.CharField(max_length=100)
    filename = models.CharField(max_length=100)
    emotions = models.CharField(max_length=100000)
    file = models.FileField(upload_to='files/')
    cdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.loginid

    class Meta:
        db_table = "UserImageEmotions"



class SurveyResponseModel(models.Model):
    user_prediction = models.ForeignKey(UserImagePredictinModel, on_delete=models.CASCADE)
    question1 = models.CharField(max_length=100, choices=RESPONSE_CHOICES)
    question2 = models.CharField(max_length=100, choices=RESPONSE_CHOICES)
    question3 = models.CharField(max_length=100, choices=RESPONSE_CHOICES)
    question4 = models.CharField(max_length=100, choices=RESPONSE_CHOICES)
    question5 = models.CharField(max_length=100, choices=RESPONSE_CHOICES)
    question6 = models.CharField(max_length=100, choices=RESPONSE_CHOICES)
    question7 = models.CharField(max_length=100, choices=RESPONSE_CHOICES)
    question8 = models.CharField(max_length=100, choices=RESPONSE_CHOICES)
    question9 = models.CharField(max_length=100, choices=RESPONSE_CHOICES)
    question10 = models.CharField(max_length=100, choices=RESPONSE_CHOICES)
    question11= models.CharField(max_length=100, choices=RESPONSE_CHOICES)
    question12= models.CharField(max_length=100, choices=RESPONSE_CHOICES)
    question13= models.CharField(max_length=100, choices=RESPONSE_CHOICES)
    question14= models.CharField(max_length=100, choices=RESPONSE_CHOICES)
    question15= models.CharField(max_length=100, choices=RESPONSE_CHOICES)
    
    # Add fields for the remaining 13 questions
    stress_level = models.CharField(max_length=100)
    survey_score = models.IntegerField()

    def __str__(self):
        return f"Survey Response - {self.user_prediction.username}"

class CombinedResultModel(models.Model):
    user_prediction = models.ForeignKey(UserImagePredictinModel, on_delete=models.CASCADE)
    survey_response = models.ForeignKey(SurveyResponseModel, on_delete=models.CASCADE)
    
    stress_level_from_image = models.CharField(max_length=100)
    emotion_from_image = models.CharField(max_length=100)
    
    # Add any additional fields you need
    
    def __str__(self):
        return f"Combined Result - {self.user_prediction.username}"

    class Meta:
        db_table = "CombinedResults"

