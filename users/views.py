from django.shortcuts import render, HttpResponse
from .forms import UserRegistrationForm
from .models import UserRegistrationModel,UserImagePredictinModel
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from .utility.GetImageStressDetection import ImageExpressionDetect
from .utility.MyClassifier import KNNclassifier
from subprocess import Popen, PIPE
import subprocess
# Create your views here.


# Create your views here.
def UserRegisterActions(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'You have been successfully registered')
            form = UserRegistrationForm()
            return render(request, 'UserRegistrations.html', {'form': form})
        else:
            messages.success(request, 'Email or Mobile Already Existed')
            print("Invalid form")
    else:
        form = UserRegistrationForm()
    return render(request, 'UserRegistrations.html', {'form': form})


def UserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginname')
        pswd = request.POST.get('pswd')
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = UserRegistrationModel.objects.get(loginid=loginid, password=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "activated":
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                print("User id At", check.id, status)
                return render(request, 'users/UserHome.html', {})
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'UserLogin.html')
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'UserLogin.html', {})


def UserHome(request):
    return render(request, 'users/UserHome.html', {})

def UploadImageForm(request):
    loginid = request.session['loginid']
    data = UserImagePredictinModel.objects.filter(loginid=loginid)
    return render(request, 'users/UserImageUploadForm.html', {'data': data})

def UploadImageAction(request):
    image_file = request.FILES['file']

    # let's check if it is a csv file
    if not image_file.name.endswith('.jpg'):
        messages.error(request, 'THIS IS NOT A JPG  FILE')

    fs = FileSystemStorage()
    filename = fs.save(image_file.name, image_file)
    # detect_filename = fs.save(image_file.name, image_file)

    # Ensure that the leading '/' is present in the URL
    

    uploaded_file_url = fs.url(filename)
    obj = ImageExpressionDetect()
    emotion = obj.getExpression(filename)
    username = request.session['loggeduser']
    loginid = request.session['loginid']
    email = request.session['email']
    UserImagePredictinModel.objects.create(username=username,email=email,loginid=loginid,filename=filename,emotions=emotion,file=uploaded_file_url)
    data = UserImagePredictinModel.objects.filter(loginid=loginid)
    return render(request, 'users/UserImageUploadForm.html', {'data':data})

def UserEmotionsDetect(request):
    
        imgname = request.GET.get('imgname')
        if imgname:
            
            obj = ImageExpressionDetect()
            emotion = obj.getExpression(imgname)
            loginid = request.session['loginid']
            data = UserImagePredictinModel.objects.filter(loginid=loginid)
            return render(request, 'users/UserImageUploadForm.html', {'data': data})
        else:
            print("Error: Image name is None")
            # Handle the error or redirect to an error page
        return render(request, 'users/UserImageUploadForm.html')

def UserLiveCameDetect(request):
    obj = ImageExpressionDetect()
    obj.getLiveDetect()
    return render(request, 'users/UserLiveHome.html', {})

def UserKerasModel(request):
    # p = Popen(["python", "kerasmodel.py --mode display"], cwd='StressDetection', stdout=PIPE, stderr=PIPE)
    # out, err = p.communicate()
    subprocess.call("python kerasmodel.py --mode display")
    return render(request, 'users/UserLiveHome.html', {})

def UserKnnResults(request):
    obj = KNNclassifier()
    df,accuracy,classificationerror,sensitivity,Specificity,fsp,precision = obj.getKnnResults()
    df.rename(columns={'Target': 'Target', 'ECG(mV)': 'Time pressure', 'EMG(mV)': 'Interruption', 'Foot GSR(mV)': 'Stress', 'Hand GSR(mV)': 'Physical Demand', 'HR(bpm)': 'Performance', 'RESP(mV)': 'Frustration', }, inplace=True)
    data = df.to_html()
    return render(request,'users/UserKnnResults.html',{'data':data,'accuracy':accuracy,'classificationerror':classificationerror,
                                                       'sensitivity':sensitivity,"Specificity":Specificity,'fsp':fsp,'precision':precision})


from .models import CombinedResultModel
from django.shortcuts import render, redirect , get_object_or_404
from .forms import SurveyResponseForm
from django.http import Http404

def calculate_survey_score(answers):
    # Assuming answers is a dictionary with keys like 'question1', 'question2', etc.
    total_score = 0

    for key, value in answers.items():
        # Extract the question number from the key
        question_number = int(key.replace('question', ''))

        # Perform the addition only if value is a valid choice
        if value in ['a', 'b', 'c', 'd']:
            # Assign scores based on your logic (you may need to adjust these)
            score_mapping = {'a': 3, 'b': 2, 'c': 1, 'd': 0}
            total_score += score_mapping[value]

    return total_score

def determine_emotion(emotions, survey_score):
    threshold = 5
    detected_emotion = interpret_detected_emotion(emotions)

    # Add more conditions for additional emotions
    if survey_score > threshold:
        if detected_emotion == 'Happy':
            return 'Happy'
        elif detected_emotion == 'Neutral':
            return 'Neutral'
        elif detected_emotion == 'Surprise':
            return 'Surprise'
        # Add more conditions for other emotions
        else:
            return 'Joy'
    else:
        return 'Sad'


def interpret_detected_emotion(emotions):
    detected_emotions = emotions.split(', ')
    
    # Map your model's emotion labels to the desired emotions
    emotion_mapping = {
        'Angry': 'Angry',
        'Disgusted': 'Disgusted',
        'Fearful': 'Fearful',
        'Sad': 'Sad',
        'Neutral': 'Neutral',
        'Surprise': 'Surprise',
        'Happy': 'Happy',
    }

    # Get the most dominant emotion
    dominant_emotion = max(detected_emotions, key=detected_emotions.count)

    # Map the detected emotion to the desired emotion
    mapped_emotion = emotion_mapping.get(dominant_emotion, 'Unknown')

    return mapped_emotion

def determine_stress_level_from_emotions(emotions):
    # Define your stress level thresholds based on your application's logic
    low_stress_threshold = 10
    moderate_stress_threshold = 20

    # Check if emotions is a dictionary
    if isinstance(emotions, dict):
        # Assuming 'emotions' is a dictionary with emotion names as keys and scores as values
        if emotions:
            total_score = sum(emotions.values()) / len(emotions)  # Calculate average score

            if total_score < low_stress_threshold:
                return 'Low Stress'
            elif low_stress_threshold <= total_score < moderate_stress_threshold:
                return 'Moderate Stress'
            else:
                return 'High Stress'
        else:
            return 'Emotions data not available'
    else:
        return 'Emotions data not available'

def determine_stress_level(survey_score):
    # Define your stress level thresholds based on your application's logic
    low_stress_threshold = 10
    moderate_stress_threshold = 20

    if survey_score < low_stress_threshold:
        return 'Low Stress'
    elif low_stress_threshold <= survey_score < moderate_stress_threshold:
        return 'Moderate Stress'
    else:
        return 'High Stress'



def SurveyResponseAction(request):
    if request.method == 'POST':
        form = SurveyResponseForm(request.POST)
        if form.is_valid():
            loginid = request.session.get('loginid')
            if loginid:
                try:
                    # Use filter to get a queryset
                    user_predictions = UserImagePredictinModel.objects.filter(loginid=loginid)


                    if user_predictions.exists():
                        # Choose one of the objects, for example, the first one
                        user_prediction = user_predictions.first()

                    survey_response = form.save(commit=False)
                    survey_response.user_prediction = user_prediction
                    survey_response.survey_score = calculate_survey_score(form.cleaned_data)
                    survey_response.save()

                    # Use 'interpret_detected_emotion' instead of 'determine_emotions_from_scores'
                    emotions = interpret_detected_emotion(user_prediction.emotions)


                    # Determine stress level from emotions
                    stress_level = determine_stress_level_from_emotions(emotions)

                    stress_level = determine_stress_level(survey_response.survey_score)

                    # Retrieve 'emotion' from cleaned_data with a default value
                    emotion = form.cleaned_data.get('emotion', '')

                    combined_result, created = CombinedResultModel.objects.get_or_create(
                        user_prediction=user_prediction,
                        survey_response=survey_response,
                        defaults={
                            'stress_level_from_image': user_prediction.emotions,
                            'emotion_from_image': emotion,
                            # Add any additional fields you need
                        }
                    )

                    if not created:
                        combined_result.stress_level_from_image = user_prediction.emotions
                        combined_result.emotion_from_image = emotion
                        combined_result.save()

                    determined_emotion = determine_emotion(user_prediction.emotions, survey_response.survey_score)

                    context = {
                        'emotion': emotion,
                        'survey_score': survey_response.survey_score,
                        'stress_level': user_prediction.emotions,
                        'stress_level_from_survey': stress_level,
                        'determined_emotion': determined_emotion,
                        
                    }

                    return render(request, 'users/CombinedResults.html', context)

                except UserImagePredictinModel.DoesNotExist:
                    messages.error(request, 'User prediction not found.')
            else:
                messages.error(request, 'Login ID not found in session.')
        else:
            messages.error(request, 'Invalid form submission. Please check your answers.')
    else:
        form = SurveyResponseForm()

    return render(request, 'users/survey_response_form.html', {'form': form})


from django.shortcuts import render
from .models import CombinedResultModel

def CombinedResultsView(request):
    # Check if the user is logged in
    loginid = request.session.get('loginid')
    if loginid:
        try:
            # Fetch the latest user prediction
            user_prediction = UserImagePredictinModel.objects.get(loginid=loginid)
            
            # Fetch the latest survey response for the user
            latest_survey_response = user_prediction.surveyresponsemodel_set.latest('timestamp')

            # Fetch the combined result for the latest survey response
            combined_result = CombinedResultModel.objects.filter(
                user_prediction=user_prediction,
                survey_response=latest_survey_response
            ).first()

            if combined_result:
                return render(request, 'users/CombinedResults.html', {
                    'emotion': combined_result.emotion_from_image,
                    'survey_score': latest_survey_response.survey_score,
                    'stress_level': determine_stress_level_from_emotions(combined_result.emotion_from_image),
                    'determined_emotion': combined_result.determined_emotion
                })
            else:
                messages.error(request, 'Combined result not found.')
        except UserImagePredictinModel.DoesNotExist:
            messages.error(request, 'User prediction not found.')
    else:
        messages.error(request, 'Login ID not found in session.')

    # Redirect to the user home or login page if there is an error
    return redirect('user_home')
