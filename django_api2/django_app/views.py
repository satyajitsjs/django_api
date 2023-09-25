from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import UserSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse , JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def studen_create(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        # print(pythondata)
        # return
        serializer = UserSerializer(data = pythondata)

        if serializer.is_valid():
            serializer.save()
            res = {"msg" : "Data created"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data , content_type = 'application/json')
            # return JsonResponse(res)
        return JsonResponse(serializer.errors)

