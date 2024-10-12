from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def getData(request):
    data = {
        'data' : {
            'en' : "Hello World",
            'pt' : "Ola Mundo",
            'no' : 'Hei Verden'
        }
    }
    return Response(data)

