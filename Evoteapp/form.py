from django.forms import ModelForm

from Evoteapp.models import Candidate_model, Complaint_model, Feedback_model, Login_model, Officer_model, User_model, Vote_model


class Candidate_modelForm(ModelForm):
    class Meta:
        model = Candidate_model
        fields=['fname','mname','lname','dob','gender','address','party','ward','logo','city','state','country','pincode','photo','aadhaar','proof','voterid','phone','mail']

class Login_modelform(ModelForm):
    class Meta:
        model = Login_model
        fields=['username','password','type']

class User_modelform(ModelForm):
    class Meta:
        model = User_model
        fields=['LOGIN_ID','name','gender','dob','mailid','mobno','photo','aadhaar']

class Feedback_modelform(ModelForm):
    class meta:
        model = Feedback_model
        fields=['feedback','user','date']
class Complaint_modelform(ModelForm):
    class meta:
        model = Complaint_model
        fields=['complaint','user','date']
class Vote_modelform(ModelForm):
    class meta:
        model = Vote_model
        fields=['candidate','vote']
class Officer_modelform(ModelForm):
    class meta:
        model = Officer_model
        fields=['LOGIN_ID','name','gender','dob','phone','mailid','photo']
       
