from django.shortcuts import render, redirect
from .models import Image

def index(request):
    return render(request,'index.html')


# Only change here is instead of using request.post we are using request.files
# Every image we upload will also have the name of the image in the name attribute of the image
def upload(request):
    Image.objects.create(image=request.FILES['image'], name=request.FILES['image'].name)
    return redirect('/success')

def success(request):
    context={
        'images':Image.objects.all()
    }
    return render(request, 'success.html', context)