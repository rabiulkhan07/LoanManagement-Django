from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from users.models import Users, Loan
from users.serializers import UsersSerializers, LoanSerializers

from django.core.files.storage import default_storage

##User Model API

@csrf_exempt
def userApi(request, id = 0):

    if request.method == 'GET':
        users = Users.objects.all()
        user_serializer = UsersSerializers(users, many=True)
        return JsonResponse(user_serializer.data, safe=False)

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UsersSerializers(data=user_data)

        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add.", safe=False)

    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user = Users.objects.get(id=user_data['id'])
        user_serializer = UsersSerializers(user, data=user_data)

        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)

    elif request.method == 'DELETE':
        user = Users.objects.get(id=id)
        user.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def SaveFile(request):
    file = request.FILES['myFile']
    file_name = default_storage.save(file.name,file)

    return JsonResponse(file_name,safe=False)


## Loan Model API

@csrf_exempt
def loanApi(request, id = 0):

    if request.method == 'GET':
        loans = Loan.objects.all()
        loan_serializer = LoanSerializers(loans, many=True)
        return JsonResponse(loan_serializer.data, safe=False)

    elif request.method == 'POST':
        loan_data = JSONParser().parse(request)
        loan_serializer = LoanSerializers(data=loan_data)

        if loan_serializer.is_valid():
            loan_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add.", safe=False)

    elif request.method == 'PUT':
        loan_data = JSONParser().parse(request)
        loan = Loan.objects.get(id=loan_data['id'])
        loan_serializer = LoanSerializers(loan, data=loan_data)

        if loan_serializer.is_valid():
            loan_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)

    elif request.method == 'DELETE':
        loan = Loan.objects.get(id=id)
        loan.delete()
        return JsonResponse("Deleted Successfully", safe=False)

