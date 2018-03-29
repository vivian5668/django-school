from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class Course:
    def __init__(self, name, description, units):
        self.name = name
        self.description = description
        self.units = units

courses = [
    Course('WDI', 'A whirlwind tour of Hell', 40),
    Course('UXDI', 'For those non-tech types', 35),
    Course('DSI', 'BIG DATA', 45)
]

def index(request):
    return render(request, 'schooltool/index.html', {'courses': courses})
    
