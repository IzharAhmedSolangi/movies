from django.db import models


class polls(models.Model):
    title= models.TextField(null=True , blank=True)
    op1 = models.CharField(max_length=100)
    op2 = models.CharField(max_length=100)
    op3 = models.CharField(max_length=100)
    op4 = models.CharField(max_length=100)

class pollsData(models.Model):
    selected_op = models.CharField(max_length=400)

class userData(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    discription = models.CharField(max_length=1000)
    

class FAQs(models.Model):
    title =models.CharField(max_length=300)
    Ans =models.CharField(max_length=3000)
    title1 =models.CharField(max_length=300)
    Ans1 =models.CharField(max_length=3000)
    title2 =models.CharField(max_length=300)
    Ans2 =models.CharField(max_length=3000)
    

