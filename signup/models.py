from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    MARITAL_STATUS_CHOICES = [
        ('Never Married','Never Married'),
        ('Widowed','Widowed'),
        ('Divorced', 'Divorced'),
        ('Awaiting divorce','Awaiting divorce')
    ]

    FAMILY_STATUS_CHOICES = [
        ('Middle class','Middle class'),
        ('Upper middle class','Upper middle class'),
        ('High class', 'High class'),
        ('Rich/Affluent','Rich/Affluent')
    ]

    FAMILY_TYPE_CHOICES = [
        ('Joint','Joint'),
        ('Nuclear','Nuclear')
       
    ]

    FAMILY_VALUES_CHOICES = [
        ('Orthodox','Orthodox'),
        ('Traditional','Traditional'),
        ('Moderate', 'Moderate'),
        ('Liberal','Liberal')
    ]

    DISABILITY_CHOICES =[
        ('None','None'),
        ('Physically challenged','Physically challenged')
    ]

    PROFILE_CHOICES = [
    ('Myself', 'Myself'),
    ('Friend', 'Friend'),
    ('Sister', 'Sister'),
    ('Brother', 'Brother'),
    ('Parent','Parent')
    ]

    GENDER_CHOICES = [
        ('Male','Male'),
        ('Female','Female')
    ]

    LANGUAGES = [
        ('Malayalam','Malayalam'),
        ('Tamil','Tamil'),
        ('Hindi','Hindi'),
        ('English','English'),
        ('Kannada','Kannada'),
        ('Telugu','Telugu')
    ]
    
    name =          models.CharField(max_length=150)
    profile =       models.CharField(max_length=150,choices=PROFILE_CHOICES,blank=True)
    email =         models.EmailField(max_length=100, unique=True,blank=True)
    password =      models.CharField(max_length=128,blank=True,null=True)
    cast =          models.CharField(max_length=15,blank=True,null=True)
    image =         models.ImageField(upload_to='profile/',default='profile/default.webp')
    height =        models.FloatField(blank=True,null=True)
    weight =        models.FloatField(blank=True,null=True)
    address =       models.CharField(max_length=255,blank=True,null=True)
    contact =       models.CharField(max_length=15,blank=True,null=True)
    dob =           models.DateField(blank=True,null=True)
    marital_status =models.CharField(max_length=20,choices=MARITAL_STATUS_CHOICES,blank=True,null=True)
    family_status = models.CharField(max_length=20,choices=FAMILY_STATUS_CHOICES,blank=True,null=True)
    family_type =   models.CharField(max_length=20,choices=FAMILY_TYPE_CHOICES,blank=True,null=True)
    family_values = models.CharField(max_length=20,choices=FAMILY_VALUES_CHOICES,blank=True,null=True)
    disability =    models.CharField(max_length=25,choices=DISABILITY_CHOICES,blank=True,null=True)
    gender =        models.CharField(max_length=20,choices=GENDER_CHOICES,blank=True,null=True)
    mother_tongue = models.CharField(max_length=50,choices=LANGUAGES,blank=True,null=True)
    about =         models.TextField(null=True)


class Admin(models.Model):

    email = models.EmailField(max_length=100, unique=True, blank=True)
    password =  models.CharField(max_length=128,blank=True,null=True)

    def set_password(self, raw_password):
        from django.contrib.auth.hashers import make_password
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password, self.password)
    
    def __str__(self):
        return self.email
    
