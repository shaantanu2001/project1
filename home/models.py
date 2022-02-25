from django.db import models

occupation_choices = (("Student","Student"), ("Faculty","Faculty"), ("Employed","Employed"), ("Other","Other"))
qualification_choices = (("High School", "High School"), ("Pre University (XII)", "Pre University (XII)")
                        ,("Diploma", "Diploma"), ("Bachelor's Degree", "Bachelor's Degree"),
                        ("Master's Degree", "Master's Degree"), ("Doctoral Degree", "Doctoral Degree"))
# Create your models here.
class CustomUser(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=10, primary_key=True)
    email = models.EmailField(('Email Address'), unique=True)
    qualification = models.CharField("Highest Qualification", max_length=30,null=True, choices=qualification_choices)
    dob = models.DateField("Date of Birth", null=True)
 
    class Meta():
        db_table = 'students'
    

