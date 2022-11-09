from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

# Create your views here.

## ------------------- FUNCTIOIN BASED VIEWS ------------------------ ##
# @csrf_exempt
# def student_data(request):
#     if request.method == 'GET':
#         pdata = json.loads(request.body)
#         id = pdata.get('id',None)
#         if id != None:
#             try:
#                 stud = Student.objects.get(id = id)
#             except Student.DoesNotExist:
#                 return HttpResponse(json.dumps({'msg' : "The required resource not found"}), content_type = 'application/json',status = 404)

#             serializer =StudentSerializer(stud)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type = 'application/json',status = 200)
#         stud = Student.objects.all()
#         serializer =StudentSerializer(stud, many = True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type = 'application/json',status = 200)
    
#     if request.method == 'POST':
#         pdata = json.loads(request.body)       
#         serializer = StudentSerializer(data = pdata) 
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg' : 'data created successfully'}
#             return HttpResponse(json.dumps(res), content_type = 'application/json',status = 200)
#         res = {'msg' : 'error occur while creating data'}
#         return HttpResponse(json.dumps(res), content_type = 'application/json',status = 500)

#     if request.method == 'PUT':
#         pdata = json.loads(request.body)
#         id = pdata.get('id')
#         try:
#             stud = Student.objects.get(id = id)
#         except Student.DoesNotExist:
#             return HttpResponse(json.dumps({'msg' : "The required resource not found"}), content_type = 'application/json',status = 404)

#         serializer = StudentSerializer(stud,data = pdata, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg' : 'data updated successfully'}
#             return HttpResponse(json.dumps(res), content_type = 'application/json',status = 200)
#         res = {'msg' : 'error occur while updating data'}
#         return HttpResponse(json.dumps(res), content_type = 'application/json',status = 500)

#     if request.method == 'DELETE':
#         pdata = json.loads(request.body)
#         id = pdata.get('id')
#         try:
#             stud = Student.objects.get(id = id)
#         except Student.DoesNotExist:
#             return HttpResponse(json.dumps({'msg' : "The required resource not found"}), content_type = 'application/json',status = 404)
        
#         stud.delete()
#         res = {'msg' : 'data deleted successfully'}
#         return HttpResponse(json.dumps(res), content_type = 'application/json',status = 500)


## ------------------- CLASS BASED VIEWS ------------------------ ##
@method_decorator(csrf_exempt, name='dispatch')
class StudentData(View):
    def get(self, request, *args, **kwargs):
        pdata = json.loads(request.body)
        id = pdata.get('id',None)
        if id != None:
            try:
                stud = Student.objects.get(id = id)
            except Student.DoesNotExist:
                return HttpResponse(json.dumps({'msg' : "The required resource not found"}), content_type = 'application/json',status = 404)

            serializer =StudentSerializer(stud)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type = 'application/json',status = 200)
        stud = Student.objects.all()
        serializer =StudentSerializer(stud, many = True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type = 'application/json',status = 200)
    
    def post(self, request, *args, **kwargs):
        pdata = json.loads(request.body)     
        roll_no = pdata.get('roll')
        try:
            stud = Student.objects.get(roll = roll_no)
        except Student.DoesNotExist:
            serializer = StudentSerializer(data = pdata) 
            if serializer.is_valid():
                serializer.save()
                res = {'msg' : 'data created successfully'}
                return HttpResponse(json.dumps(res), content_type = 'application/json',status = 200)

            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type = 'application/json',status = 400)

        return HttpResponse(json.dumps({'msg' : 'student already exists'}), content_type = 'application/json',status = 400)
        
    def put(self, request, *args, **kwargs):
        pdata = json.loads(request.body)
        id = pdata.get('id')
        try:
            stud = Student.objects.get(id = id)
        except Student.DoesNotExist:
            return HttpResponse(json.dumps({'msg' : "The required resource not found"}), content_type = 'application/json',status = 404)

        serializer = StudentSerializer(stud,data = pdata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'data updated successfully'}
            return HttpResponse(json.dumps(res), content_type = 'application/json',status = 200)

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json',status = 400)

    def delete(self, request, *args, **kwargs):
        pdata = json.loads(request.body)
        id = pdata.get('id')
        try:
            stud = Student.objects.get(id = id)
        except Student.DoesNotExist:
            return HttpResponse(json.dumps({'msg' : "The required resource not found"}), content_type = 'application/json',status = 404)
        
        stud.delete()
        res = {'msg' : 'data deleted successfully'}
        return HttpResponse(json.dumps(res), content_type = 'application/json',status = 500)












