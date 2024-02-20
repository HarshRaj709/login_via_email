from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from .forms import UserRegistration,UserLogin,ProfileUser


# Create your views here.
def signup(request):
    if request.method == 'POST':
        fm = UserRegistration(request.POST)
        if fm.is_valid():
            f_name = fm.cleaned_data['firstName']
            l_name = fm.cleaned_data['lastName']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            username = fm.cleaned_data['username']
            user = User(first_name=f_name,last_name=l_name,email=email,username=username)
            user.set_password(password)
            user.save()
            return redirect('login')
        else:
            return render(request,'app/Signup.html',{'form':fm})
    else:
        fm =UserRegistration()
        return render(request,'app/Signup.html',{'form':fm})



# def signup(request):
#     if request.method == 'POST':
    #     f_name= request.POST['firstName']
    #     l_name = request.POST['lastName']
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     username = request.POST['username']
    #     if f_name == '':
    #         messages.error(request,'Please enter First Name')
    #         return render(request,'app/Signup.html',{'username':username,'lastName':l_name,'email':email,'password':password})
    #     if l_name == '':
    #         messages.error(request,'Please enter Last Name')
    #         return render(request,'app/Signup.html',{'username':username,'firstName':f_name,'email':email,'password':password})
    #     if username == '':
    #         messages.error(request,'Please Select your UserName')
    #         return render(request,'app/Signup.html',{'firstName':f_name,'lastName':l_name,'email':email,'password':password})
    #     if email == '':
    #         messages.error(request,'Please Enter Your Email')
    #         return render(request,'app/Signup.html',{'firstName':f_name,'lastName':l_name,'username':username,'password':password})
    #     # Validate email format
    #     try:
    #         validate_email(email)
    #     except ValidationError:
    #         messages.error(request, 'Please Enter a valid Email')
    #         return render(request, 'app/Signup.html', {'firstName': f_name, 'lastName': l_name, 'username': username, 'password': password})
        
    #     if(User.objects.filter(username=username).exists()):
    #         messages.error(request,'Username already taken..Please try with different Username')
    #         return render(request,'app/Signup.html',{'firstName':f_name,'lastName':l_name,'email':email,'password':password})
    #     if(User.objects.filter(email=email).exists()):
    #         messages.error(request,'Email already taken..Please try with different Email')
    #         return render(request,'app/Signup.html',{'firstName':f_name,'lastName':l_name,'username':username,'password':password})
    #     user = User.objects.create_user(username=username,first_name=f_name,last_name=l_name,email=email,password=password)
    #     user.save()
    #     messages.success(request,'User created successfully')
    #     return redirect('login')
    # else:
    #     return render(request,'app/Signup.html')

def login1(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = UserLogin(request.POST)
            if fm.is_valid():
                username = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                user = authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Login Successful')
                    return redirect('profile')
                else:
                    messages.error(request,'Wrong Credentials')
                    return redirect('login')

        else:
            return render(request,'app/login.html')
    else:
        return redirect('profile')

    
# def login1(request):
#     if not request.user.is_authenticated:
#         if request.method == 'POST':
#             username = request.POST['username']
#             password = request.POST['password']
#             user = authenticate(username=username,password=password)
#             if user is not None:
#                 login(request,user)
#                 messages.success(request,'Login Successful')
#                 return redirect('profile')
            # else:
            #     messages.error(request,'Wrong Credentials')
            #     return redirect('login')
#         else:
#             return render(request,'app/login.html')
#     else:
#         return redirect('profile')
    


# def profile(request):
#     fm = ProfileUser(instance=request.user)
#     return render(request,'app/profile.html',{'user':fm})


@login_required(login_url='login')  #here you can specify your specific login url rather than to specify it in settings.py
def profile(request):
    my_user = request.user
    return render(request,'app/profile.html',{'user':my_user})