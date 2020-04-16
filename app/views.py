from django.contrib.auth.decorators import user_passes_test
from app import serializers
from app.models import Files, CustomUser
from app import serializers
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import json
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

# Create your views here.


@csrf_exempt
@api_view(["POST"])
@permission_classes([AllowAny])
def create_user(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        print(request.data)
        first_name = request.data['firstName']
        last_name = request.data['lastName']
        email = request.data['email']
        username = request.data['username']
        password = request.data['password']

        data = CustomUser.objects.create_user(first_name, last_name,
                                              email, username, password)
        serializer = serializers.UserSerializer(data)

        return JsonResponse({"success": serializer.data}, safe=False)


@csrf_exempt
@api_view(["POST"])
def upload(request):
    """
    List all code snippets, or create a new snippet.
    """

    if request.method == 'POST':
        a = {}
        userID = request.POST.get('id')
        print(userID)
        ID = CustomUser.objects.get(id=userID)
        print(ID.username)
        for filename, file in request.FILES.items():
            size = request.POST.get(filename)
            a[request.FILES[filename].name] = (request.FILES[filename].name)
            data = Files.objects.create(
                fileName=request.FILES[filename].name, fileLocation=request.FILES[filename], fileSize=size, userID=ID)
            data.save()
        return JsonResponse({"success": a}, safe=False)


@csrf_exempt
@api_view(["POST"])
def download(request):

    if request.method == 'POST':

        userID = request.data
        print(userID)
        data = Files.objects.filter(userID=userID)
        print(data)
        serializer = serializers.DownloadSerializer(
            data, many=True, context={'request': request})
        return JsonResponse({"success": serializer.data}, safe=False)


@csrf_exempt
@api_view(["POST"])
def get_ID(request):

    if request.method == 'POST':
        
        user_name = request.data['username']
        print(user_name)
        user = CustomUser.objects.get(username=user_name)  

        return JsonResponse({"ID": user.id,"isAdmin": user.is_superuser}, safe=False)


@csrf_exempt
@api_view(["POST"])
def fileDelete(request):

    if request.method == 'POST':

        files = request.data
        print(files)
        for file in files:
            Files.objects.get(id=file).delete()

        return JsonResponse({"success": files}, safe=False)


# try:
#   person = People.objects.get(Name='Fred')
# except (People.DoesNotExist):
#   # Do something else...
class IsSuperUser(IsAdminUser):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)






@csrf_exempt
@api_view(["GET"])
def AdminUser(request):

    if request.method == "GET":
        is_staff = CustomUser.objects.get(email=request.user)
        if (is_staff.is_superuser):
                
            userData= CustomUser.objects.all()            
            serializer = serializers.UserSerializer(userData, many=True)
            print(serializer.data)
            return JsonResponse({"success": serializer.data}, safe=False)
        else:
            return JsonResponse({"error": "Invalid request"},safe=False)
