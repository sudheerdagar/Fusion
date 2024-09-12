from rest_framework import serializers
from .models import *
from applications.academic_information.models import Student
from applications.globals.models import Designation,HoldsDesignation

class PreviousWinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Previous_winner
        fields = '__all__'
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class AwardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award_and_scholarship
        fields = '__all__'

class McmSerializer(serializers.ModelSerializer):
    student=StudentSerializer()
    award_id=AwardsSerializer()
    class Meta:
        model = Mcm
        fields = '__all__'

class DirecorGoldMedalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director_gold
        fields = '__all__'

class DirectorSilverMedalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director_silver
        fields = '__all__'

class ProficiencyDMSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proficiency_dm
        fields = '__all__'

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'

class HoldsDesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoldsDesignation
        fields = '__all__'
