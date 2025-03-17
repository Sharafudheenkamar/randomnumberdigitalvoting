from Evoteapp.models import Candidate_model, Candidatecode_model, Complaint_model, Feedback_model, Login_model, Officer_model, User_model, UserCandidateCode, Vote_model
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class loginserializer(ModelSerializer):
    class Meta:
        model = Login_model
        fields = ['username','password','type']

class userserializer(ModelSerializer):
     name = serializers.CharField(source='LOGIN_ID.username', read_only=True)
     password = serializers.CharField(source='LOGIN_ID.password', read_only=True)
     class Meta:
        model = User_model
        fields = ['LOGIN_ID','name','gender','dob','age','mailid','address','mobno','photo','aadhaar','voterid', 'name', 'password']

class feedbackserializer(ModelSerializer):
    class Meta:
        model = Feedback_model
        fields = ['feedback','user']

class complaintserializer(ModelSerializer):
    class Meta:
        model = Complaint_model
        fields = ['complaint','user']

class voteserializer(ModelSerializer):
    class Meta:
        model = Vote_model
        fields = ['candidate','vote']
    
class Candidateserializer(ModelSerializer):
    class Meta:
        model = Candidate_model
        fields = ['fname','mname','lname','aadhaar','dob','gender','address','party','ward','city','state','country','pincode','mail','phone','voterid','logo','proof','photo']

class  Officerserializer(ModelSerializer):
    class Meta:
        model = Officer_model
        fields = ['LOGIN_ID','name','dob','gender','mailid','phone','photo']

class CandidateCodeSerializer(ModelSerializer):
    class Meta:
        model = Candidatecode_model
        fields = ['code','candidate','voter']


class UserCandidateCodeserializer(ModelSerializer):
    class Meta:
        model = UserCandidateCode
        fields = '__all__'
        