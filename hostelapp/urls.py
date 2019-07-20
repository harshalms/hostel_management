from django.urls import path
from hostelapp.views import hello, hostel, student, mess


urlpatterns = [
    path('hello/', hello),
    path('hostel/', hostel),
    path('student/', student),
    path('mess/', mess)
]