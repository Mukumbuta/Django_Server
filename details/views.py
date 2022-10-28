from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from details.models import SlackDetails
from details.serializers import SlackDetailsSerializer

@api_view(['GET'])
def slack_Details(request):
    if request.method == 'GET':
        data =  {
                "slackUserName": "Emmanuel Simasiku",
                "backend": True,
                "age": 30,
                "bio": "A passionate Software developer with a passion for developing innovative programs that expedite the efficiency and effectiveness of organizational success. I spend my free time painting or watching movies."
            }
        return Response(data)