from django.http import JsonResponse

# Create your views here.
def index_view(request):
    return JsonResponse({"data" : 'Hello World'})