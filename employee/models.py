from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    cv=models.FileField(upload_to='cv/')
    contact_number=models.IntegerField()
    Linked_in=models.URLField(null=True)
    website=models.URLField(max_length=40,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)




    def __str__(self):
        return self.username

class Skill(models.Model):
    skill=models.TextField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



    def __str__(self):
        return self.skill


class Experience(models.Model):

    company=models.CharField(max_length=20)
    designation=models.CharField(max_length=30)
    duration=models.DurationField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.company

