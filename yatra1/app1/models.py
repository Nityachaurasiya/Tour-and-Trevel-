from django.db import models

# Create your models here.
class student(models.Model):
    st_name=models.CharField(max_length=50,null=True)
    st_email=models.EmailField(max_length=70,null=True)
    st_phone=models.CharField(max_length=20,null=True)
    st_gender=models.CharField(max_length=70,null=True)
    st_seating=models.CharField(max_length=70,null=True)
    st_diet=models.CharField(max_length=70,null=True)
    st_handicap=models.CharField(max_length=70,null=True)
    st_address=models.CharField(max_length=70,null=True)
    st_country=models.CharField(max_length=70,null=True)

def __self__(self):
    return self.st_name



class user(models.Model):
    st_name=models.CharField(max_length=50,null=True)
    st_email=models.EmailField(max_length=70,null=True)
    st_password=models.CharField(max_length=20,null=True)

def __self__(self):
    return self.st_name


# class contactEnquiry(models.Model):
#     name=models.CharField(max_length=50,null=True)
#     email=models.EmailField(max_length=70,null=True)
#     msg_box=models.CharField(max_length=70,null=True)

# def __self__(self):
#     return self.name