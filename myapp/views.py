import uuid
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import UserProfile
from .serializers import UserProfileSerializer
from django.contrib.auth.hashers import check_password, make_password

@api_view(['POST'])
def signup(request):
    data = request.data
    data['password'] = make_password(data['password'])
    data['api_key'] = str(uuid.uuid4())[:40]  # Generate a unique API key
    serializer = UserProfileSerializer(data=data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response({'api_key': data['api_key']}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def signupProcess(request, api_key):
    try:
        user = UserProfile.objects.get(api_key=api_key)
    except UserProfile.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    data = request.data
    serializer = UserProfileSerializer(instance=user, data=data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def signin(request):
    email = request.data.get('email', '')
    password = request.data.get('password', '')

    try:
        user = UserProfile.objects.get(email=email)
    except UserProfile.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    if not check_password(password, user.password):
        return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)

    return Response({'api_key': user.api_key}, status=status.HTTP_200_OK)

@api_view(['GET'])
def viewUserData(request, api_key):
    try:
        user = UserProfile.objects.get(api_key=api_key)
    except UserProfile.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserProfileSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PATCH'])
def updateUser(request, api_key):
    try:
        user = UserProfile.objects.get(api_key=api_key)
    except UserProfile.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserProfileSerializer(instance=user, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logout(request, api_key):
    try:
        user = UserProfile.objects.get(api_key=api_key)
    except UserProfile.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    # Invalidate the user's API key (you might want to remove it from the database)
    user.api_key = None
    user.save()

    return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def deleteAccount(request, api_key):
    try:
        user = UserProfile.objects.get(api_key=api_key)
    except UserProfile.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    # Delete the user account (you might want to perform additional cleanup)
    user.delete()

    return Response({'message': 'Account deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['PATCH'])
def changePassword(request, api_key):
    try:
        user = UserProfile.objects.get(api_key=api_key)
    except UserProfile.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    current_password = request.data.get('current_password', '')
    new_password = request.data.get('new_password', '')

    # Check if the current password is correct
    if not user.check_password(current_password):
        return Response({'error': 'Invalid current password'}, status=status.HTTP_401_UNAUTHORIZED)

    # Update the user's password
    user.password = make_password(new_password)
    user.save()

    return Response({'message': 'Password changed successfully'}, status=status.HTTP_200_OK)

"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from django.http import JsonResponse    
from .models import UserProfile
from django.contrib import messages
import datetime
from django.db.models import Max

def start(request):
    return render(request, 'myapp/start.html')

def home(request):
    return render(request, 'myapp/home.html')

def food(request):
    return render(request, 'myapp/food.html')

def signupProcess(request):
    return render(request, 'myapp/signupProcess.html')

def diet(request):
    return render(request, 'myapp/diet.html')

def dietProcess(request):
    return render(request, 'myapp/dietProcess.html')

def meal(request):
    return render(request, 'myapp/meal.html')

def mealProcess(request):
    return render(request, 'myapp/mealProcess.html')

def fitness(request):
    return render(request, 'myapp/fitness.html')

def fitnessProcess(request):
    return render(request, 'myapp/fitnessProcess.html')

def lastSignup(request):
    return render(request, 'myapp/lastSignup.html')

def signup(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_profile = UserProfile.objects.create(
            email=email,
            phone_number=phone_number,
            password=password,
        )

        return redirect('food')

    else:
        form = SignUpForm()
    return render(request, 'myapp/signup.html')

def signupProcess(request):
    id = UserProfile.objects.aggregate(max_id=Max('id'))['max_id']
    print(id)
    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        current_weight = request.POST.get('current_weight')
        current_height = request.POST.get('current_height')
        bmi = request.POST.get('bmi')
        education_details = request.POST.getlist('education_details')
        occupation = request.POST.getlist('occupation')
        medical_conditions = request.POST.getlist('medical_conditions')

        obj_update = UserProfile.objects.get(pk=id)
        obj_update.name = name
        obj_update.gender = gender
        obj_update.age = age
        obj_update.current_weight = current_weight
        obj_update.current_height = current_height
        obj_update.bmi = bmi
        obj_update.education_details = education_details
        obj_update.occupation = occupation
        obj_update.medical_condition = medical_conditions

        obj_update.save()

        return redirect('diet')

        # user_profile = UserProfile.objects.update(
        #     name=name,  
        #     gender=gender,
        #     age=age,
        #     current_weight=current_weight,
        #     current_height=current_height,
        #     bmi=bmi,
        #     education_details=education_details,
        #     occupation=occupation,
        #     medical_conditions=medical_conditions
        # )
        # print(user_profile)
        
        # return JsonResponse({'success': True, 'message': 'Account created successfully'})
        # form = SignUpForm(request.POST)
        # print(form)
        # if form.is_valid():
        #     user = form.save()
        #     login(request, user)
        #     return redirect('home')
    
    else:
        pass
        # form = SignUpForm()
    return render(request, 'myapp/signupProcess.html') #, {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, email=email, password=password)
        print(user)

        if user is not None:
            # Log the user in
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('base')  
        else:
            messages.error(request, 'Invalid login credentials.')
    else:
        form = LoginForm()

    return render(request, 'myapp/login.html', {'form': form})"""