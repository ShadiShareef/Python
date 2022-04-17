from django.db import models

class Checkerror(models.Manager):
    def validator(self, Data):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(Data['first_name']) < 2:
            errors["first_name"] = "Blog name should be at least 5 characters"
        if len(Data['last_name']) < 2:
            errors["last_name"] = "Blog name should be at least 5 characters"
        if len(Data['email']) < 2:
            errors["email"] = "Blog name should be at least 5 characters"
        if len(Data['Password']) < 8:
            errors["Password"] = "Password should be at least 10 characters"
        return errors

# Create your models here.
class User(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects= Checkerror()
# def addUserDB(request,context):

#     User.objects.create(first_name=context['firstName'],last_name=context['lastName'],email_name=context['eMail'],password=context['passWord'])
#     return