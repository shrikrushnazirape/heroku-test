from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from .models import Student
from PIL import Image, ImageFont, ImageDraw

# Create your views here.
def index(request):
    if request.method == "POST":
        data = request.POST
        name = data['name']
        roll = data['roll_no']
        try:
            getuser = Student.objects.get(name = name)
            na = getuser.certi
            return render(request, 'participant/success.html', {'user':getuser})
        except:
            return HttpResponse("invalid user data")
     
    return render(request, 'participant/index.html')


