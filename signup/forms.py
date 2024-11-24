from django import forms
from .models import Profile



class SignupForm(forms.ModelForm):
    # Profile = forms.ChoiceField(choices=PROFILE_CHOICES, widget=forms.Select(attrs={
    #     'class': 'profile-select',
    #     # 'style': ' width: 55%; height:20px; position: relative; left: 25px;'  # Inline styles for testing
    # }))
    class Meta:
        model = Profile
        fields = ['name', 'profile','email','password']
        widgets = {
           
            'name': forms.TextInput(attrs={'class': 'form-control name-input','placeholder':'Enter name'}),
            'profile': forms.Select(attrs={'class': 'form-control custom-select custom-width','placeholder':'-Select-'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control email-input','placeholder':'Enter email id'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control password-input','placeholder':'Enter password'}),

        }

class profile_details_form(forms.ModelForm):
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Profile
        fields = ['dob','gender','weight','height','address','contact','image','marital_status','family_status','family_type','family_values','disability','mother_tongue','about']
        widgets = {
           
           
            'gender' : forms.Select,
            'address': forms.TextInput(attrs={'placeholder': 'Enter your address'}),
            'contact': forms.TextInput(attrs={'placeholder': 'Enter your contact number'}),
            'image' : forms.FileInput,
            'marital_status' : forms.Select,
            'family_status': forms.Select,
            'family_type': forms.Select,
            'family_values': forms.Select,
            'disability': forms.Select,
            'weight' : forms.NumberInput,
            'height' : forms.NumberInput,
            'mother_tongue' : forms.Select,
            'about' : forms.Textarea,

        }
        labels ={
            'dob' : 'Date of Birth',
            'disability':'Any Disability'
        }

class ProfileForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Profile
        fields = ['name', 'profile','email','password','dob', 'gender', 'weight', 'height', 'address', 'contact', 'image', 
                  'marital_status', 'family_status', 'family_type', 'family_values', 
                  'disability', 'mother_tongue', 'about']
        widgets = {


            'name': forms.TextInput(attrs={'class': 'form-control name-input','placeholder':'Enter name'}),
            'profile': forms.Select(attrs={'class': 'form-control custom-select custom-width','placeholder':'-Select-'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control email-input','placeholder':'Enter email id'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control password-input','placeholder':'Enter password'}),
            'gender' : forms.Select,
            'address': forms.TextInput(attrs={'placeholder': 'Enter your address'}),
            'contact': forms.TextInput(attrs={'placeholder': 'Enter your contact number'}),
            'image' : forms.FileInput,
            'marital_status' : forms.Select,
            'family_status': forms.Select,
            'family_type': forms.Select,
            'family_values': forms.Select,
            'disability': forms.Select,
            'weight' : forms.NumberInput,
            'height' : forms.NumberInput,
            'mother_tongue' : forms.Select,
            'about' : forms.Textarea,
        
        #      'name': forms.TextInput(attrs={'class': 'form-control name-input','placeholder':'Enter name'}),
        #     'profile': forms.Select(attrs={'class': 'form-control custom-select custom-width','placeholder':'-Select-'}),
        #     'email' : forms.EmailInput(attrs={'class' : 'form-control email-input','placeholder':'Enter email id'}),
        #     'password': forms.PasswordInput(attrs={'class': 'form-control password-input','placeholder':'Enter password'}),
        #     'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        #     'gender': forms.Select(attrs={'class': 'form-control'}),
        #     'weight': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'height': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'address': forms.TextInput(attrs={'class': 'form-control'}),
        #     'contact': forms.TextInput(attrs={'class': 'form-control'}),
        #     'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        #     'marital_status': forms.Select(attrs={'class': 'form-control'}),
        #     'family_status': forms.Select(attrs={'class': 'form-control'}),
        #     'family_type': forms.Select(attrs={'class': 'form-control'}),
        #     'family_values': forms.Select(attrs={'class': 'form-control'}),
        #     'disability': forms.TextInput(attrs={'class': 'form-control'}),
        #     'mother_tongue': forms.TextInput(attrs={'class': 'form-control'}),
        #     'about': forms.Textarea(attrs={'class': 'form-control'}),
        # 
        }

        labels ={
            'dob' : 'Date of Birth',
            'disability':'Any Disability'
        }
