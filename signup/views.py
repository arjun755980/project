from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import mysql.connector as sql
from .forms import SignupForm
from .forms import profile_details_form
from .forms import ProfileForm
from .models import Profile
from django.urls import reverse
from datetime import date,timedelta
from django.contrib import messages
from .models import Admin


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
           profile = form.save()
           request.session['profile_id'] = profile.id
           user =User.objects.create_user(username=profile.email,email=profile.email,password=profile.password)
           user.save()

           return redirect(reverse('profile_view',args=[profile.id] ))
    else:
         form = SignupForm()
    return render(request, 'register.html', {'form': form})

@login_required
def home_view(request,user_email):
    user = get_object_or_404(Profile, email=user_email)
    opposit_sexx =  'Male' if user.gender =='Female' else 'Female'
    user_profile = get_object_or_404(Profile,email=request.user.email)
    opposit_sex = 'Male' if user_profile.gender =='Female' else 'Female'
    pros = Profile.objects.filter(gender = opposit_sexx)
    age_range=5
    user_age_is = date.today().year - user.dob.year
    user_age = (date.today()- user.dob).days // 365
    if user.gender == 'Male':
         min_date_of_birth = date.today() - timedelta(days=(user_age_is + age_range) * 365)
         max_date_of_birth = user.dob + timedelta(days= 3 * 365)
         similar_profiles = Profile.objects.filter(
             gender = opposit_sexx,
             dob__gte = min_date_of_birth,
             dob__lte = max_date_of_birth
          )
    else:
        max_date_of_birth = date.today() - timedelta(days=(user_age_is + age_range) * 365)
        similar_profiles = Profile.objects.filter(
            gender = opposit_sexx,
            dob__gte = max_date_of_birth,
            dob__lte = user.dob,
        )
    context = {
        'user_profile': user,
        'similar_profiles': similar_profiles,
        'pros' : pros,
        'age' : user_age
    }

    return render(request,'Home.html', context)

@login_required
def edit_view(request,user_email):
    
    profile = get_object_or_404(Profile, email=user_email)

    if request.method =='POST':
        profile.name=request.POST.get('name',profile.name)
        profile.dob=request.POST.get('dob',profile.dob)
        profile.marital_status=request.POST.get('marital_status',profile.marital_status)
        profile.family_status=request.POST.get('family_status',profile.family_status)
        profile.family_values=request.POST.get('family_values',profile.family_values)    # profile = get_object_or_404(Profile, email=user_email)
        profile.height=request.POST.get('height',profile.height)
        profile.weight=request.POST.get('weight',profile.weight)
        profile.address=request.POST.get('address',profile.address)
        profile.family_type=request.POST.get('family_type',profile.family_type)
        profile.disability=request.POST.get('disability',profile.disability)
        profile.cast=request.POST.get('cast',profile.cast)
        profile.contact=request.POST.get('contact',profile.contact)
        profile.mother_tongue=request.POST.get('mother_tongue',profile.mother_tongue)
        profile.about=request.POST.get('about',profile.about)
        profile.save()
        return redirect(reverse('home',args=[profile.email]))
    # if request.method == 'POST':
    #     new_value = request.POST.get(field)

    #     if field in ['gender', 'address', 'contact']:  # Add other fields as needed
    #         setattr(profile, field, new_value)
    #         profile.save()
    #         return redirect('profile')  # Change 'profile' to your profile view name

    return render(request,'edit.html',{'profile':profile})

def profile_view(request,profile_id):
    # profile_id = request.session.get('profile_id')
    # if not profile_id :
    #     return redirect('web1')
    profile = get_object_or_404(Profile, id=profile_id)
    if request.method == 'POST' :
        form = profile_details_form(request.POST, request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            # del request.session['profile_id']
            context = {
                'name' : profile.name,
                'image' : profile.image
            }
            # return redirect(reverse('home'),context)
            messages.success(request,"Successfully Created user...")
            return redirect('welcome')
    else:
        form = profile_details_form()
    return render(request, 'profile.html',{'form' : form})

# views.py
from django.shortcuts import  get_object_or_404
from .models import Profile

@login_required
def profile_details(request, email):
    user = get_object_or_404(Profile, email=email)


    
    return render(request, 'profile_view.html', {'user1': user})

def login_view(request):
    global email,password
    if request.method == 'POST':
        # m=sql.connect(host="localhost",user="root",passwd="Geometry+3",database="matrimony")
        # cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                email=value
            if key=="password":
                password=value
        # c = "SELECT * FROM signup_profile WHERE email=%s AND  password = %s"
        # values=(email,password)
        # cursor.execute(c,values)
        # t=tuple(cursor.fetchall())
        # if t==():
        #     return render(request,'error.html')
        # else:
        #     user_details=t[0]
        #     context ={
        #         'user_name' :user_details[1],
        #         'user_pic' : user_details[6],
                
        #     }
        user = authenticate(request,username=email,password=password)
        if user is not None:
            messages.success(request,'Successfully logged in...')
            login(request,user)
        else:
            pass
        request.session['user_email'] = email
        return redirect(reverse('home',args=[email] ))
            # return render(request,'Home.html',context)
    return render(request,'login.html')

# def login_view(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         try:
#             user = User.objects.get(email=email)
#             user = authenticate(username=user.username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 return render(request, 'login.html', {'error': 'Invalid login credentials'})
#         except User.DoesNotExist:
#             return render(request, 'login.html', {'error': 'User with this email does not exist'})

#     return render(request, 'login.html')
def welcome_view(request):
    # user = Profile.objects.filter(gender = 'Female')
    
    # context = {
    #     'user' : user
    # }

    return render(request,'welcome.html')

def logout_view(request):
    logout(request)
    return render(request,'welcome.html')

def admin_login(request):
    # global email,password
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        # d=request.POST
        # for key,value in d.items():
        #     if key=="email":
        #         email=value
        #     if key=="password":
        #         password=value
        try:
             admin = Admin.objects.get(email=email)
             if admin.check_password(password):
           
                 request.session['admin_id'] = admin.id
                 return redirect('admin_dashboard')
             else:
            
                 messages.error(request,'Incorrect password. Please try again.')
        except Admin.DoesNotExist:
            messages.error(request,'No admin found with that email.')
    return render(request, 'admin_login.html') 

def admin_dashboard(request): 
    if 'admin_id' in request.session:

        users = Profile.objects.all()
        return render(request, 'admin_dashboard.html',{'users':users})
    else:
        return redirect(request,'admin_login.html')

def create_profie(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            profile = form.save(commit = False)
            password = form.cleaned_data.get('password')
            user =User.objects.create_user(username=profile.email,email=profile.email)
            user.set_password(password)
            user.save()
            profile.save()
            return redirect('admin_dashboard')
    else:
        form = ProfileForm()

    return render(request, 'add_user.html',{'form': form})