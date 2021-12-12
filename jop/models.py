from django.db import models


JOPTYPE=(('FULL TIME','FULL TIME'),
         ('PART TIME','PART TIME'))
class jop(models.Model):

     title=models.CharField(max_length=100)

     job_type=models.CharField(max_length=20,choices=JOPTYPE)

     description=models.TextField(max_length=5000)
     publishedat=models.DateTimeField(auto_now=True)
     Vacancy=models.IntegerField(default=1)
     salary=models.IntegerField(default=0)
     experience=models.IntegerField(default=1)
     category=models.ForeignKey('Category',on_delete=models.CASCADE)

     def __str__(self):
          return self.title

class Category (models.Model):
     name=models.CharField(max_length=25)

     def __str__(self):
          return self.name