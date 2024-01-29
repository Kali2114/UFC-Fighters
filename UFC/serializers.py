from django.contrib.auth.models import User
from rest_framework import serializers

from UFC.models import Fighter, FightingStyle


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class FightingStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FightingStyle
        fields = ['fight_style']

class FighterSerializer(serializers.HyperlinkedModelSerializer):
    belt = serializers.StringRelatedField()
    fighting_styles = FightingStyleSerializer(many=True)
    class Meta:
        model = Fighter
        fields = ['name', 'country', 'age', 'description', 'record',
                   'profile_picture', 'belt', 'fighting_styles']
