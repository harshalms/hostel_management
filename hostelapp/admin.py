from django.contrib import admin
from hostelapp.models import Hostel, Student, Staff, StudentRoom, Mess, Room
# Register your models here.
admin.site.register(Hostel)
admin.site.register(Student)
admin.site.register(Room)
admin.site.register(Staff)
admin.site.register(Mess)
admin.site.register(StudentRoom)
