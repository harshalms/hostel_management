from django.db import models
from datetime import datetime

# Create your models here.

class Hostel(models.Model):
    hostel_name=models.CharField(max_length=50)
    total_rooms=models.IntegerField()
    address=models.CharField(max_length=100)
    created_on=models.DateField(auto_now=True)
    updated_on=models.DateField(auto_now=True)

    def __str__(self):
        return self.hostel_name

class Student(models.Model):
    name=models.CharField(max_length=50)
    roll_no=models.IntegerField(unique=True)
    email=models.EmailField(max_length=100, default='')
    phone=models.CharField(max_length=15, null=True)
    created_on=models.DateField(auto_now=True)
    updated_on=models.DateField(auto_now=True)
    department = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Room(models.Model):
    room_no=models.CharField(max_length=50)
    hostel=models.ForeignKey(Hostel, on_delete=models.CASCADE)
    created_on=models.DateField(auto_now=True)
    updated_on=models.DateField(auto_now=True)

    def __str__(self):
        return str(self.hostel.hostel_name + ' -> '+ self.room_no)

class Staff(models.Model):
    name=models.CharField(max_length=50)
    post=models.CharField(max_length=50)
    phone=models.CharField(max_length=15, null=True)
    email=models.EmailField(max_length=100, default='')
    created_on=models.DateField(auto_now=True)
    updated_on=models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Mess(models.Model):
    mess_name=models.CharField(max_length=50)
    created_on=models.DateField(auto_now=True)
    updated_on=models.DateField(auto_now=True)
    
    def __str__(self):
        return self.mess_name

class StudentRoom(models.Model):
    room=models.ForeignKey(Room, on_delete=models.CASCADE)
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    is_occupied=models.BooleanField()
    created_on=models.DateField(auto_now=True)
    updated_on=models.DateField(auto_now=True)

class HostelStaff(models.Model):
    hostel=models.ForeignKey(Hostel, on_delete=models.CASCADE)
    staff=models.ForeignKey(Staff, on_delete=models.CASCADE)
    is_active=models.BooleanField()

    def __str__(self):
        return str(self.hostel.hostel_name + ' -> '+ self.staff.name)



