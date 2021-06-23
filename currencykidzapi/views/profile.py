from currencykidzapi.models.withdrawal_event import WithdrawalEvent
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from currencykidzapi.models import Saver, DepositEvent, WithdrawalEvent


class ProfileView(ViewSet):
    """Saver can see profile information"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single profile """

        try:
            profile = Saver.objects.get(pk=pk)
            serializer = SaverSerializer(profile, context={'request': request})
            return Response(serializer.data)
        except Exception:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for a saver

        Returns:
            Response -- Empty body with 204 status code
        """

        saver = Saver.objects.get(user=request.auth.user)
        saver.profile_image_url = request.data["profile_image_url"]
        saver.goal_amount = request.data["goal_amount"]
        saver.created_on = request.data["created_on"]

        saver.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def list(self, request):
        """Handle GET requests to profile resource

        Returns:
            Response -- JSON representation of user info and events
        """
        saver = Saver.objects.get(user=request.auth.user)
        deposit_events = DepositEvent.objects.filter(saver=saver)
        withdrawal_events = WithdrawalEvent.objects.filter(saver=saver)

        # many=True is telling the serializer there is more than one thing to serialize.
        deposit_events = DepositEventSerializer(
            deposit_events, many=True, context={'request': request})
        withdrawal_events = WithdrawalEventSerializer(
            withdrawal_events, many=True, context={'request': request})
        saver = SaverSerializer(
            saver, many=False, context={'request': request})

        # Manually construct the JSON structure you want in the response
        # data is the dictionary version of the saver object
        # this chunk is creating a new dictionary.
        profile = {}
        profile["saver"] = saver.data
        profile["deposit_events"] = deposit_events.data
        profile["withdrawal_events"] = withdrawal_events.data
        # Response is turning the profile dictionary into JSON.
        return Response(profile)

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for saver's related Django user"""
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')


class SaverSerializer(serializers.ModelSerializer):
    """JSON serializer for savers"""
    user = UserSerializer(many=False)

    class Meta:
        model = Saver
        fields = ('id', 'user', 'profile_image_url', 'created_on', 'goal_amount')


class DepositEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = DepositEvent
        fields = ('id', 'date', 'name', 'sound_effect', 'total')

class WithdrawalEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = WithdrawalEvent
        fields = ('id', 'date', 'name', 'sound_effect', 'total')