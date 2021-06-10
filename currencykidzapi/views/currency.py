from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from currencykidzapi.models import Currency


class CurrencyView(ViewSet):

    def list(self, request):
        """Handle GET requests to get all currency

        Returns:
            Response -- JSON serialized list of currency
        """
        currency = Currency.objects.all()

        # Note the addtional `many=True` argument to the
        # serializer. It's needed when you are serializing
        # a list of objects instead of a single object.
        serializer = CurrencySerializer(
            currency, many=True, context={'request': request})
        return Response(serializer.data)

class CurrencySerializer(serializers.ModelSerializer):
    """JSON serializer for currency

    Arguments:
        serializers
    """
    class Meta:
        # What model to use and what keys in the model to use.
        model = Currency
        fields = ('id',
                'quarter',
                'dime',
                'nickel',
                'penny',
                'one_dollar',
                'five_dollars',
                'ten_dollars',
                'twenty_dollars',
                'fifty_dollars',
                'one_hundred_dollars')