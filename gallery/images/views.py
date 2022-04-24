from django.shortcuts import render
from .models import images, albums

def hub(request):
    return render(request, 'images/hub.html')

def view_image(request, primary):
    return render(request, 'images/view_image.html')

def upload_image(request):
    return render(request, 'images/upload_image.html')

def album(request):
    albums = images.objects.all()
    context = {'albums': albums}
    return render(request, 'images/album.html', context)