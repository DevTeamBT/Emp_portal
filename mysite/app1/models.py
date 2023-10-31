from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# class bodhtree(models.Model):

class Employee(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    id=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    designation=models.CharField(max_length=30)
    department=models.CharField(max_length=20)
    reports_to=models.CharField(max_length=20)
    date_of_joining=models.DateField(default=date.today)
    work_type=models.CharField(max_length=20)
    annual_ctc=models.IntegerField()
    office_email=models.EmailField()
    work_location=models.CharField(max_length=20)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    mobile = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    personal_email=models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    state= models.CharField(max_length=15)


    class Meta:
        db_table = 'employee_details'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
