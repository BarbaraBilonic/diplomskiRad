from django.db import models



class Project(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.TextField(max_length=1000)


class TestPlan(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.TextField(max_length=1000)
    startDate=models.DateField(auto_now=False,auto_now_add=False)
    endDate=models.DateField(auto_now=False,auto_now_add=False)
    project=models.ForeignKey('Project',on_delete=models.CASCADE)
    statusId=models.ForeignKey('Status',on_delete=models.SET_NULL, null=True)

class TestObjective(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.TextField(max_length=1000,null=False,blank=False)
    testPlanId=models.ForeignKey('TestPlan',on_delete=models.CASCADE)
    statusId=models.ForeignKey('Status',on_delete=models.SET_NULL,null=True,default=1)

class Test(models.Model):
    id=models.AutoField(primary_key=True)
    testObjectiveId=models.ForeignKey('TestObjective',on_delete=models.CASCADE)
    name=models.TextField(max_length=1000)
    description=models.TextField(max_length=3000)
    testSteps=models.TextField(max_length=3000,null=True,blank=True)
    statusId=models.ForeignKey('Status',on_delete=models.SET_NULL, null=True, default=1)
    testerId=models.ForeignKey('User',on_delete=models.SET_NULL, null=True)

class TestResult(models.Model):
    id=models.AutoField(primary_key=True)
    testId=models.ForeignKey('Test',on_delete=models.CASCADE)
    result=models.TextField(max_length=10)
    date=models.DateTimeField(auto_now_add=True)
    testerId=models.ForeignKey('User',on_delete=models.SET_NULL, null=True)
    

class Status(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.TextField(max_length=30)


class User(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.TextField(max_length=50)
    lastName=models.TextField(max_length=50)
    roleId=models.ForeignKey('Role',on_delete=models.SET_NULL,null=True)
    email=models.TextField(max_length=250)
    password=models.TextField(max_length=200)
    username=models.TextField(max_length=30)


class Role(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.TextField(max_length=20)
    description=models.TextField(max_length=1000)