from django.http import HttpResponse, JsonResponse

def get_json(request):
    return JsonResponse({"name":"jake","age":25})

