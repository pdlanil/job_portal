from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Company_Profile(models.Model):

    company_name=models.CharField(max_length=100)
    address=models.CharField(max_length=40)
    website=models.URLField(max_length=40,null=True,blank=True)
    contact_no=models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)



    def __str__(self):
            return self.company_name



class Job(models.Model):

    title=models.CharField(max_length=20,null=False)
    description=models.TextField(null=False)
    deadline=models.DateField()
    company_id=models.ForeignKey(Company_Profile,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
