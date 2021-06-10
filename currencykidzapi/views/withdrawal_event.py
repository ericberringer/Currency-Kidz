from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from currencykidzapi.models import WithdrawalEvent, Saver, Currency, saver

class WithdrawalEventView(ViewSet):

    def create(self, request):
        """Handle POST operations for withdrawal_events

        Returns:
            Response -- JSON serialized withdrawal_event instance
        """
        saver = Saver.objects.get(user=request.auth.user)
        # user=request.auth.user is basically a WHERE in sql

        withdrawal_event = WithdrawalEvent()
        withdrawal_event.name = request.data["name"]
        withdrawal_event.total = request.data["total"]
        withdrawal_event.date = request.data["date"]
        withdrawal_event.sound_effect = request.data["sound_effect"]
        withdrawal_event.saver = saver


        currency = Currency.objects.get(pk=request.data["currency"])
        withdrawal_event.currency = currency

        try:
            withdrawal_event.save()
            serializer = WithdrawalEventSerializer(withdrawal_event, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single event

        Returns:
            Response -- JSON serialized game instance
        """
        try:
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(event, context={'request': request})
            return Response(serializer.data)
        except Exception:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for an event

        Returns:
            Response -- Empty body with 204 status code
        """
        organizer = Gamer.objects.get(user=request.auth.user)

        event = Event.objects.get(pk=pk)
        event.event_name = request.data["eventName"]
        event.description = request.data["description"]
        event.date = request.data["date"]
        event.game = request.data["gameId"]
        event.time = request.data["time"]
        event.attendees = request.data["attendees"]
        event.organizer = organizer

        game = Game.objects.get(pk=request.data["gameId"])
        event.game = game
        event.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single withdrawal_event

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            withdrawal_event = WithdrawalEvent.objects.get(pk=pk)
            withdrawal_event.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except WithdrawalEvent.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to withdrawal_event resource

        Returns:
            Response -- JSON serialized list of withdrawal_events
        """
        
        withdrawal_events = WithdrawalEvent.objects.all()

        serializer = WithdrawalEventSerializer(
            withdrawal_events, many=True, context={'request': request})

        return Response(serializer.data)

# In these serializers we are specifying what we want to come back, the fields variable is where we are specifying what we
# want included in the data that is coming back. Using depth you can access an entire object of an entire nested object.

class WithdrawalEventUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

class WithdrawalEventSaverSerializer(serializers.ModelSerializer):
    user = WithdrawalEventUserSerializer(many=False)

    class Meta:
        model = Saver
        fields = ['user', 'profile_image_url', 'goal_amount', 'created_on']

class WithdrawalEventSerializer(serializers.ModelSerializer):
    """JSON serializer for withdrawal_events"""
    saver = WithdrawalEventSaverSerializer(many=False)

    class Meta:
        model = WithdrawalEvent
        fields = ('id', 'saver', 'name', 'date', 'currency', 'total', 'sound_effect')
        depth = 1

