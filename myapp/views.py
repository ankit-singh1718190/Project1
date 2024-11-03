from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def Studentget(request):
    stu=Student.objects.all()
    serializer = StudentSerializer(stu,many=True) # Serializing the student object
    json_data = JSONRenderer().render(serializer.data)  # Rendering serialized data as JSON
    return HttpResponse(json_data, content_type='application/json')
 
@csrf_exempt
def studentCreate(request):
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pytonData=JSONParser().parse(stream)
        ComplexData=StudentSerializer(data=pytonData)
        if ComplexData.is_valid():
            ComplexData.save()
            res={'msg':'data Created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(ComplexData.errors)
        return HttpResponse(json_data,content_type='application/json')
