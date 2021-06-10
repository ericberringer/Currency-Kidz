from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from currencykidzapi.models import DepositEvent, Saver, Currency, saver

class DepositEventView(ViewSet):

    def create(self, request):
        """Handle POST operations for deposit_events

        Returns:
            Response -- JSON serialized deposit_event instance
        """
        deposit_event = DepositEvent()
        deposit_event.name = request.data["name"]
        deposit_event.total = request.data["total"]
        deposit_event.date = request.data["date"]
        deposit_event.sound_effect = request.data["sound_effect"]

        saver = Saver.objects.get(pk=request.data['saver'])
        deposit_event.saver = saver

        currency = Currency.objects.get(pk=request.data["currency"])
        deposit_event.currency = currency

        try:
            deposit_event.save()
            serializer = DepositEventSerializer(deposit_event, context={'request': request})
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
        """Handle DELETE requests for a single game

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            event = Event.objects.get(pk=pk)
            event.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Event.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to deposit_event resource

        Returns:
            Response -- JSON serialized list of deposit_events
        """
        deposit_events = DepositEvent.objects.all()

        serializer = DepositEventSerializer(
            deposit_events, many=True, context={'request': request})

        return Response(serializer.data)

# In these serializers we are specifying what we want to come back, the fields variable is where we are specifying what we
# want included in the data that is coming back. Using depth you can access an entire object of an entire nested object.

class DepositEventUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

class DepositEventSaverSerializer(serializers.ModelSerializer):
    user = DepositEventUserSerializer(many=False)

    class Meta:
        model = Saver
        fields = ['user', 'profile_image_url', 'goal_amount', 'created_on']

class DepositEventSerializer(serializers.ModelSerializer):
    """JSON serializer for deposit_events"""
    saver = DepositEventSaverSerializer(many=False)

    class Meta:
        model = DepositEvent
        fields = ('id', 'saver', 'name', 'date', 'saver', 'currency', 'total', 'sound_effect')

